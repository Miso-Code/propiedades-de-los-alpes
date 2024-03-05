import json
from flask import request, Response

from ..modules.agent.application.mappers import AutomationAgentDTOJsonMapper
from ..modules.agent.application.queries.get_agent_by_id import GetAgent
from ..modules.agent.application.services import AgentService
from ..seedwork.application.queries import execute_query

from ..seedwork.domain.exceptions import DomainException
from ..seedwork.presentation.api import create_blueprint

bp = create_blueprint('agent', '/agent')


@bp.route('/automation', methods=('POST',))
def agent():
    try:
        agent_dict = request.json

        mapper = AutomationAgentDTOJsonMapper()
        agent_dto = mapper.external_to_dto(agent_dict)
        agent_service = AgentService()
        final_dto = agent_service.create_automation_agent(agent_dto)

        return mapper.dto_to_external(final_dto)
    except DomainException as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')


@bp.route('/automation', methods=('GET',))
@bp.route('/automation/<agent_id>', methods=('GET',))
def get_automation_agent(agent_id=None):
    try:
        agent_service = AgentService()
        if agent_id:
            query_result = execute_query(GetAgent(agent_id))
            return AutomationAgentDTOJsonMapper().dto_to_external(query_result.result)
        else:
            return [{"id": str(agent_id), "error": "Not Implemented"}]
    except DomainException as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')