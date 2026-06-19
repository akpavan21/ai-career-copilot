from pydantic import BaseModel, Field
from typing import List


class ResumeAnalysisRequest(BaseModel):
    resume_text: str = Field(..., min_length=10)
    job_description: str = Field(..., min_length=10)


class InterviewRequest(BaseModel):
    target_role: str
    skills: List[str]


class LearningPathRequest(BaseModel):
    current_skills: List[str]
    missing_skills: List[str]
    target_role: str
