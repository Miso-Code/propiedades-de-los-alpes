import json
from flask import request, Response

from ..modules.ingestion.application.mappers import PropertyIngestionDTOJsonMapper
from ..modules.ingestion.application.commands.create_ingestion import CreatePropertyIngestionCommand
from ..modules.ingestion.application.services import PropertyIngestionService
from ..modules.ingestion.infrastructure.dispatchers import Dispatcher

from ..seedwork.application.commands import execute_command
from ..seedwork.domain.exceptions import DomainException
from ..seedwork.presentation.api import create_blueprint

bp = create_blueprint('ingestion', '/ingestion')

dispatcher = Dispatcher()


@bp.route('/', methods=('POST',))
def ingestion():
    try:
        ingestion_dict = request.json

        mapper = PropertyIngestionDTOJsonMapper()
        property_ingestion_dto = mapper.external_to_dto(ingestion_dict)
        property_ingestion_service = PropertyIngestionService()
        final_dto = property_ingestion_service.create_property_ingestion(property_ingestion_dto)

        return mapper.dto_to_external(final_dto)
    except DomainException as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')


@bp.route('/', methods=('GET',))
def get_all_ingestions():
    try:
        property_ingestion_service = PropertyIngestionService()
        ingestions = property_ingestion_service.get_all_ingestions()
        return ingestions
    except DomainException as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')


@bp.route('/async', methods=('POST',))
def ingestion_async():
    try:
        ingestion_dict = request.json

        mapper = PropertyIngestionDTOJsonMapper()
        property_ingestion_dto = mapper.external_to_dto(ingestion_dict)
        command = CreatePropertyIngestionCommand(property_ingestion_dto)

        dispatcher.publish_command(command, "property-ingestion-commands")

        return Response('{}', status=202, mimetype='application/json')
    except DomainException as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
