from fastapi import APIRouter
from backend.app.api.schemas import Query
from backend.app.agents.supervisor import graph
from backend.app.agents.prompts import SYSTEM_PROMPT
from backend.app.services.orchestration import parse_response

router = APIRouter()

@router.post("/ask")
async def ask(query: Query):
    inputs = {
        "messages": [
            ("system", SYSTEM_PROMPT),
            ("user", query.message),
        ]
    }

    stream = graph.stream(inputs, stream_mode="updates")
    tool, response = parse_response(stream)

    return {
        "response": response,
        "tool_called": tool,
    }
