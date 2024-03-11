import json
import sys

from flask import request, Response

from ..modules.properties.application.queries.get_all_properties import GetAllProperties
from ..modules.properties.application.mappers import PropertyDTOJsonMapper
from ..modules.properties.infrastructure.dispatchers import Dispatcher
from ..modules.properties.application.commands.register_property import RegisterPropertiesCommand

from ..seedwork.application.queries import execute_query
from ..seedwork.domain.exceptions import DomainException
from ..seedwork.presentation.api import create_blueprint

bp = create_blueprint('properties_and_transactions', '/properties_and_transactions')
dispatcher = Dispatcher()


@bp.route('/', methods=('GET',))
@bp.route('/<id>', methods=('GET',))
def get_all_properties(id=None):
    try:
        if id:
            return {'message': 'GET!'}
        else:
            query_result = execute_query(GetAllProperties())
            map_result = PropertyDTOJsonMapper()
            return [map_result.dto_to_external(result) for result in query_result.result]

    except DomainException as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')


@bp.route('/', methods=('POST',))
def post_properties():
    try:
        property_dict = request.json

        mapper = PropertyDTOJsonMapper()
        property_properties_dto = mapper.external_to_dto(property_dict)

        command = RegisterPropertiesCommand(
            agent_id=property_properties_dto.agent_id
            , property_id=property_properties_dto.property_id
            , property_address=property_properties_dto.property_address
            , property_city=property_properties_dto.property_city
            , property_state=property_properties_dto.property_state
            , property_zip=property_properties_dto.property_zip
            , property_price=property_properties_dto.property_price
            , property_bedrooms=property_properties_dto.property_bedrooms
            , property_bathrooms=property_properties_dto.property_bathrooms
            , property_square_feet=property_properties_dto.property_square_feet
            , property_lot_size=property_properties_dto.property_lot_size
            , property_type=property_properties_dto.property_type
        )
        dispatcher.publish_validated_event(command.__dict__, "property-transactions-event")

        return Response("{}", status=202, mimetype='application/json')

    except DomainException as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')


@bp.route('/degrade', methods=('POST',))
def degrade():
    sys.exit("Degrading the service D;")
