import React, { useState } from 'react';
import { createRoot } from 'react-dom/client';
import './styles.css';

type AnalysisResult = {
  ats_score: number;
  matched_skills: string[];
  missing_skills: string[];
  recommendations: string[];
  keyword_matches: string[];
};

const sampleResume = 'Python FastAPI React TypeScript AWS PostgreSQL LangChain OpenAI RAG';
const sampleJD = 'Need AI Engineer with Python, FastAPI, AWS, LangGraph, RAG, PostgreSQL, Docker and LLM experience';

function App() {
  const [resumeText, setResumeText] = useState(sampleResume);
  const [jobDescription, setJobDescription] = useState(sampleJD);
  const [result, setResult] = useState<AnalysisResult | null>(null);
  const [loading, setLoading] = useState(false);

  async function analyzeResume() {
    setLoading(true);
    const response = await fetch('http://localhost:8000/api/resumes/analyze', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ resume_text: resumeText, job_description: jobDescription }),
    });
    const data = await response.json();
    setResult(data);
    setLoading(false);
  }

  return (
    <main className="container">
      <section className="hero">
        <h1>AI Career Copilot</h1>
        <p>Analyze resumes, compare job descriptions, identify gaps, and prepare for interviews.</p>
      </section>

      <section className="grid">
        <div className="card">
          <h2>Resume Text</h2>
          <textarea value={resumeText} onChange={(e) => setResumeText(e.target.value)} />
        </div>
        <div className="card">
          <h2>Job Description</h2>
          <textarea value={jobDescription} onChange={(e) => setJobDescription(e.target.value)} />
        </div>
      </section>

      <button onClick={analyzeResume} disabled={loading}>{loading ? 'Analyzing...' : 'Analyze Resume'}</button>

      {result && (
        <section className="results">
          <div className="score">ATS Score: {result.ats_score}%</div>
          <div className="grid">
            <ResultCard title="Matched Skills" items={result.matched_skills} />
            <ResultCard title="Missing Skills" items={result.missing_skills} />
            <ResultCard title="Keyword Matches" items={result.keyword_matches} />
            <ResultCard title="Recommendations" items={result.recommendations} />
          </div>
        </section>
      )}
    </main>
  );
}

function ResultCard({ title, items }: { title: string; items: string[] }) {
  return <div className="card"><h3>{title}</h3><ul>{items.map((item) => <li key={item}>{item}</li>)}</ul></div>;
}

createRoot(document.getElementById('root')!).render(<App />);
