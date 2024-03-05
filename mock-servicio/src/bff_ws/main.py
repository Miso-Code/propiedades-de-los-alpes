from os import getenv

from colorama import Fore, Style
from fastapi import FastAPI, Request
import asyncio
import requests

from pydantic_settings import BaseSettings
from typing import Any, Dict

from starlette.websockets import WebSocket

from .consumers import subscribe_to_topic


class Config(BaseSettings):
    APP_VERSION: str = "1"


settings = Config()
app_configs: dict[str, Any] = {"title": "BFF-Web AeroAlpes"}

app = FastAPI(**app_configs)
tasks = list()
events_by_agent: Dict[str, list] = dict()

data_ingestion_url = getenv("DATA_INGESTION_URL", "http://localhost:5000")


@app.on_event("startup")
async def app_startup():
    global tasks
    global events_by_agent
    task1 = asyncio.ensure_future(
        subscribe_to_topic("property-events", "alpes-bff", "public/default/PropertyCreatedEvent", events=events_by_agent))
    tasks.append(task1)


@app.on_event("shutdown")
def shutdown_event():
    global tasks
    for task in tasks:
        task.cancel()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    async def receive_messages():
        # Task to continuously receive messages from the client
        while True:
            data = await websocket.receive_json()
            agent_id = data.get('agent_id')
            if agent_id:
                print(Fore.LIGHTBLUE_EX, "Starting property ingestion for agent_id: {agent_id}!", Style.RESET_ALL)
                requests.post(f"{data_ingestion_url}/ingestion/", json=data)

    async def send_events():
        # Task to continuously check for and send new events to the client
        while True:
            for agent_id, events in events_by_agent.items():
                if events:  # If there are events for the agent
                    await websocket.send_json({'data': events.pop(), 'event': 'PropertyCreatedEvent'})
            await asyncio.sleep(1)

    # Run both tasks concurrently
    receive_task = asyncio.create_task(receive_messages())
    send_task = asyncio.create_task(send_events())

    # Wait for either task to complete (which will likely be when the connection closes)
    done, pending = await asyncio.wait(
        {receive_task, send_task},
        return_when=asyncio.FIRST_COMPLETED,
    )

    # Cancel the pending task to clean up
    for task in pending:
        task.cancel()

    # Await the cancelled task to suppress cancellation exceptions
    try:
        await asyncio.gather(*pending)
    except asyncio.CancelledError:
        pass
