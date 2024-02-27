from ....seedwork.application.handlers import Handler


class HandleAgentDomain(Handler):

    @staticmethod
    def handle_property_ingestion_started(event):
        print(f'Ingestion started for agent. Ingestion: {event}')
