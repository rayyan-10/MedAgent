from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage
from backend.app.config import GROQ_API_KEY


def query_medgemma(prompt: str) -> str:
    system_prompt = """
You are Dr. Emily Hartman, a warm and experienced clinical psychologist.

Style:
- Emotional attunement
- Gentle normalization
- Practical coping guidance
- Strength-focused encouragement

Rules:
- No diagnosis
- No medication
- Ask open-ended questions
"""

    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.4,
        api_key=GROQ_API_KEY,
    )

    response = llm.invoke([
        SystemMessage(content=system_prompt),
        HumanMessage(content=prompt),
    ])

    return response.content.strip()
