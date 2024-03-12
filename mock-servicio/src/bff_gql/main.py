from typing import Any

from fastapi import FastAPI
from pydantic_settings import BaseSettings

from src.bff_gql.api.v1.router import router as v1


class Config(BaseSettings):
    APP_VERSION: str = "v1.0.0"


settings = Config()
app_configs: dict[str, Any] = {"title": "BFF-Property ingestion | Propiedades de los Alpes"}

app = FastAPI(**app_configs)
tasks = list()
events = list()

app.include_router(v1, prefix="/v1")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
