from langchain.tools import tool
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent

from backend.app.tools.therapy import query_medgemma
from backend.app.tools.emergency import call_emergency
from backend.app.agents.prompts import SYSTEM_PROMPT
from backend.app.config import GROQ_API_KEY


@tool
def ask_mental_health_specialist(query: str) -> str:
    """
    Generate a therapeutic response using the MedGemma model.
    Use this for all general user queries, mental health questions, emotional concerns,
    or to offer empathetic, evidence-based guidance in a conversational tone.
    """

    return query_medgemma(query)


@tool
def emergency_call_tool() -> None:
    """
    Place an emergency call to the safety helpline's phone number via Twilio.
    Use this only if the user expresses suicidal ideation, intent to self-harm,
    or describes a mental health emergency requiring immediate help.
    """
    call_emergency()


tools = [ask_mental_health_specialist, emergency_call_tool]

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.2,
    api_key=GROQ_API_KEY,
)

graph = create_react_agent(llm, tools=tools)
