# Architecture Notes

The MVP separates the application into a React dashboard and a FastAPI service layer. The backend uses deterministic scoring so it can run locally without an OpenAI key. The `langgraph_workflow.py` file shows where a production LangGraph state machine should be connected.

## Production Upgrade Path

1. Store resumes, job descriptions, and analysis history in PostgreSQL.
2. Add pgvector, Pinecone, FAISS, or Chroma for embedding search.
3. Connect OpenAI or Amazon Bedrock for richer resume rewriting and interview simulation.
4. Add authentication using Cognito, Auth0, or JWT.
5. Deploy backend to AWS ECS/EKS or Lambda containers and frontend to S3 + CloudFront.
