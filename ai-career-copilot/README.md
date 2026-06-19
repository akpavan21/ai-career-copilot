# AI Career Copilot

AI Career Copilot is a full-stack AI platform for resume optimization, ATS scoring, job description matching, skill-gap detection, learning-path generation, and mock interview preparation.

## Problem Statement

Job seekers often fail at early screening because resumes are not aligned to ATS filters, job descriptions, required skills, and role-specific interview expectations.

## Solution

This project analyzes a resume and job description, computes ATS alignment, identifies missing skills, recommends targeted resume improvements, creates a personalized learning path, and generates mock interview questions using a FastAPI backend and React TypeScript dashboard.

## Tech Stack

Frontend: React, TypeScript, Vite

Backend: FastAPI, Python, Pydantic

AI Layer: OpenAI-ready service layer, LangChain/LangGraph-ready orchestration, RAG-style document retrieval

Database: PostgreSQL-ready schema and service layer

Cloud: AWS-ready Docker deployment pattern

## Architecture

```text
Resume Upload / JD Input
        ↓
React TypeScript Dashboard
        ↓
FastAPI Backend APIs
        ↓
Resume Parser + ATS Scoring
        ↓
LangChain/OpenAI Service Layer
        ↓
RAG Document Retriever
        ↓
Skill Gap + Learning Path Engine
        ↓
Interview Preparation Dashboard
```

## Main Features

- Resume and job description analysis
- ATS keyword scoring
- Skill-gap identification
- Personalized learning roadmap
- Mock interview question generation
- Resume improvement recommendations
- Cloud-ready API structure

## Local Setup

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload --port 8000
```

Open API docs:

```text
http://localhost:8000/docs
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Open UI:

```text
http://localhost:5173
```

## Example API Request

```bash
curl -X POST http://localhost:8000/api/resumes/analyze   -H "Content-Type: application/json"   -d '{"resume_text":"Python FastAPI AWS LangChain", "job_description":"Need AI Engineer with Python, FastAPI, AWS, RAG, LangGraph"}'
```

## Resume Points

- Developed an AI-powered career guidance platform leveraging LangChain, OpenAI-ready services, and Retrieval-Augmented Generation patterns to perform resume analysis and job matching.
- Implemented ATS scoring, skill-gap analysis, mock interview question generation, and personalized learning recommendations.
- Designed scalable REST APIs using FastAPI, Pydantic models, and modular service layers for resume intelligence workflows.
- Built a React TypeScript dashboard to visualize ATS score, matched skills, missing skills, learning roadmap, and interview preparation outputs.

## GitHub Repository Name

`ai-career-copilot`
