from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.models import ResumeAnalysisRequest, InterviewRequest, LearningPathRequest
from app.services.resume_intelligence import analyze_resume, generate_interview_questions, build_learning_path

app = FastAPI(title="AI Career Copilot API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "ai-career-copilot"}


@app.post("/api/resumes/analyze")
def resume_analysis(request: ResumeAnalysisRequest):
    return analyze_resume(request.resume_text, request.job_description)


@app.post("/api/interviews/questions")
def interview_questions(request: InterviewRequest):
    return generate_interview_questions(request.target_role, request.skills)


@app.post("/api/learning/path")
def learning_path(request: LearningPathRequest):
    return build_learning_path(request.current_skills, request.target_role, request.missing_skills)
