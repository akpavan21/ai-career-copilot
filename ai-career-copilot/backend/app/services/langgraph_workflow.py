# LangGraph workflow placeholder for production agent orchestration.
#
# Install langgraph and langchain-openai, configure OPENAI_API_KEY, then replace the simple
# service layer with this graph-based flow:
#
# START -> parse_resume -> score_ats -> retrieve_context -> skill_gap -> interview_prep -> END

from typing import TypedDict, List, Dict


class CareerState(TypedDict):
    resume_text: str
    job_description: str
    ats_score: float
    missing_skills: List[str]
    recommendations: List[str]
    retrieved_context: List[Dict]


def build_career_agent_graph():
    # Keep this separate so the MVP can run without external LLM credentials.
    # Production implementation should use StateGraph from langgraph.graph.
    raise NotImplementedError("Connect LangGraph StateGraph here for production orchestration.")
