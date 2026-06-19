import re
from collections import Counter
from typing import Dict, List

CORE_SKILLS = [
    "python", "fastapi", "react", "typescript", "aws", "postgresql",
    "openai", "langchain", "langgraph", "rag", "vector database",
    "embeddings", "llm", "api", "docker", "kubernetes", "sql"
]


def _tokens(text: str) -> List[str]:
    return re.findall(r"[a-zA-Z][a-zA-Z0-9+.#-]*", text.lower())


def _skill_hits(text: str, skills: List[str]) -> List[str]:
    lowered = text.lower()
    return sorted({skill for skill in skills if skill in lowered})


def _top_keywords(text: str, limit: int = 20) -> List[str]:
    stop_words = {"and", "the", "with", "for", "using", "from", "that", "this", "are", "will", "you", "our", "job"}
    counts = Counter(token for token in _tokens(text) if token not in stop_words and len(token) > 2)
    return [word for word, _ in counts.most_common(limit)]


def analyze_resume(resume_text: str, job_description: str) -> Dict:
    resume_skills = _skill_hits(resume_text, CORE_SKILLS)
    jd_skills = _skill_hits(job_description, CORE_SKILLS)
    missing_skills = sorted(set(jd_skills) - set(resume_skills))
    matched_skills = sorted(set(resume_skills) & set(jd_skills))

    jd_keywords = set(_top_keywords(job_description, 25))
    resume_keywords = set(_top_keywords(resume_text, 50))
    keyword_matches = sorted(jd_keywords & resume_keywords)
    ats_score = round((len(keyword_matches) / max(len(jd_keywords), 1)) * 100, 2)

    recommendations = []
    if missing_skills:
        recommendations.append(f"Add hands-on project or resume bullets for: {', '.join(missing_skills)}.")
    if ats_score < 75:
        recommendations.append("Increase job-description keyword alignment in summary, skills, and project bullets.")
    recommendations.append("Use measurable impact statements for AI, backend, cloud, and dashboard work.")

    return {
        "ats_score": ats_score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "jd_keywords_detected": sorted(jd_keywords),
        "keyword_matches": keyword_matches,
        "recommendations": recommendations,
        "rag_context": build_retrieval_context(job_description),
    }


def build_retrieval_context(job_description: str) -> List[Dict]:
    # Lightweight RAG-style retrieval placeholder.
    # In production, replace this with OpenAI embeddings + pgvector/Pinecone/FAISS/Chroma.
    knowledge_base = [
        {"topic": "RAG", "content": "RAG improves LLM output by retrieving relevant enterprise documents before generation."},
        {"topic": "LangGraph", "content": "LangGraph supports stateful multi-step agent workflows with conditional routing."},
        {"topic": "FastAPI", "content": "FastAPI is used for high-performance Python APIs with Pydantic validation."},
        {"topic": "ATS", "content": "ATS scoring compares resume content with job description keywords and required skills."},
    ]
    jd_words = set(_tokens(job_description))
    ranked = []
    for item in knowledge_base:
        score = len(jd_words & set(_tokens(item["content"] + " " + item["topic"])))
        ranked.append({**item, "score": score})
    return sorted(ranked, key=lambda x: x["score"], reverse=True)[:3]


def generate_interview_questions(target_role: str, skills: List[str]) -> Dict:
    questions = []
    for skill in skills[:8]:
        questions.append(f"How have you used {skill} in a production {target_role} project?")
        questions.append(f"What challenges did you face with {skill}, and how did you solve them?")
    return {"target_role": target_role, "questions": questions}


def build_learning_path(current_skills: List[str], target_role: str, missing_skills: List[str]) -> Dict:
    roadmap = []
    for index, skill in enumerate(missing_skills, start=1):
        roadmap.append({
            "week": index,
            "skill": skill,
            "goal": f"Build one practical mini-task using {skill} for {target_role} responsibilities.",
            "project_task": f"Add {skill} evidence to AI Career Copilot and document it in README."
        })
    return {"target_role": target_role, "current_skills": current_skills, "roadmap": roadmap}
