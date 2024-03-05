import json
from flask import request, Response

from ..modules.ingestion.application.mappers import PropertyIngestionDTOJsonMapper
from ..modules.ingestion.application.commands.create_ingestion import CreatePropertyIngestionCommand
from ..modules.ingestion.application.queries.get_all_ingestions import GetAllIngestions
from ..modules.ingestion.application.services import PropertyIngestionService
from ..modules.ingestion.infrastructure.dispatchers import Dispatcher
from ..seedwork.application.queries import execute_query

from ..seedwork.domain.exceptions import DomainException
from ..seedwork.presentation.api import create_blueprint

bp = create_blueprint('ingestion', '/ingestion')

dispatcher = Dispatcher()


@bp.route('/', methods=('GET',))
@bp.route('/<id>', methods=('GET',))
def get_all_ingestions(id=None):
    try:
        if id:
            return {'message': 'GET!'}
        else:
            query_result = execute_query(GetAllIngestions())
            map_ingestion = PropertyIngestionDTOJsonMapper()
            return [map_ingestion.dto_to_external(result) for result in query_result.result]

    except DomainException as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')


@bp.route('/', methods=('POST',))
def create_ingestion_async():
    try:
        ingestion_dict = request.json

        mapper = PropertyIngestionDTOJsonMapper()
        property_ingestion_dto = mapper.external_to_dto(ingestion_dict)
        command = CreatePropertyIngestionCommand(
            agent_id=property_ingestion_dto.agent_id
            , location_city_name=property_ingestion_dto.location_city_name
            , location_city_code=property_ingestion_dto.location_city_code
            , location_country_name=property_ingestion_dto.location_country_name
            , location_country_code=property_ingestion_dto.location_country_code
            , location_address=property_ingestion_dto.location_address
            , location_building=property_ingestion_dto.location_building
            , location_floor=property_ingestion_dto.location_floor
            , location_inner_code=property_ingestion_dto.location_inner_code
            , location_coordinates_latitude=property_ingestion_dto.location_coordinates_latitude
            , location_coordinates_longitude=property_ingestion_dto.location_coordinates_longitude
            , location_additional_info=property_ingestion_dto.location_additional_info
            , property_type=property_ingestion_dto.property_type
            , property_subtype=property_ingestion_dto.property_subtype
            , rooms=property_ingestion_dto.rooms
            , bathrooms=property_ingestion_dto.bathrooms
            , parking_spaces=property_ingestion_dto.parking_spaces
            , construction_area=property_ingestion_dto.construction_area
            , land_area=property_ingestion_dto.land_area
            , price=property_ingestion_dto.price
            , currency=property_ingestion_dto.currency
            , price_per_m2=property_ingestion_dto.price_per_m2
            , price_per_ft2=property_ingestion_dto.price_per_ft2
            , property_url=property_ingestion_dto.property_url
            , property_images=property_ingestion_dto.property_images
        )

        # This would create an integration command that would be consumed by the same module
        # This would allow us to decouple the ingestion process from the API
        dispatcher.publish_command(command, "property-ingestion-commands")

        return Response('{}', status=202, mimetype='application/json')
    except DomainException as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
