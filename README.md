# UW Governed Agent Platform

A governed, retrieval-augmented AI agent platform for healthcare use cases, built with pgvector, FastAPI, and Claude.

## Overview

This platform demonstrates a layered architecture for building safe, auditable AI agents with:
- **Retrieval-Augmented Generation (RAG)** over synthetic patient data
- **Governance guardrails** for safe healthcare AI
- **Supervised orchestration** for multi-step reasoning
- **Evaluation harness** for quality assurance

## Quickstart

```bash
# 1. Copy env template and fill in secrets
cp .env.example .env

# 2. Start infrastructure
docker-compose up -d

# 3. Install dependencies
pip install -r requirements.txt

# 4. Ingest data
python scripts/run_ingest.py

# 5. Ask a question
python scripts/ask.py "What medications is patient 123 on?"
```

## Architecture

See [ARCHITECTURE.md](ARCHITECTURE.md) for the full system design.

## Layers

| Layer | Location | Description |
|-------|----------|-------------|
| 1 – Ingest | `src/ingest/` | Source → resumable batched embedding job |
| 2 – Retrieval | `src/retrieval/` | pgvector store with swappable retriever interface |
| 3 – Agent | `src/agent/` | Health agent with tool use |
| 4 – Governance | `src/governance/` | Guardrails, PII redaction, audit logging |
| 5 – Orchestration | `src/orchestration/` | Supervisor for multi-agent coordination |
| 6 – API | `src/api/` | FastAPI REST endpoints |
| 7 – Eval | `eval/` | Golden set evaluation harness |

## Requirements

- Python 3.11+
- Docker + Docker Compose
- PostgreSQL 15+ with pgvector extension
- Anthropic API key
