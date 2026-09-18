# Architecture

## System Diagram

```
                        ┌─────────────────────────────────────────┐
                        │              Client / UI                │
                        └──────────────────┬──────────────────────┘
                                           │ HTTP
                        ┌──────────────────▼──────────────────────┐
                        │           FastAPI  (src/api/)           │
                        └──────────────────┬──────────────────────┘
                                           │
                        ┌──────────────────▼──────────────────────┐
                        │       Supervisor (src/orchestration/)   │
                        └──────┬───────────────────────┬──────────┘
                               │                       │
               ┌───────────────▼──────┐   ┌───────────▼───────────┐
               │  Health Agent        │   │  Governance / Guards  │
               │  (src/agent/)        │   │  (src/governance/)    │
               └───────────┬──────────┘   └───────────────────────┘
                           │
               ┌───────────▼──────────┐
               │  Retriever Interface │
               │  (src/retrieval/)    │
               └───────────┬──────────┘
                           │
               ┌───────────▼──────────┐
               │  pgvector / Postgres │
               └──────────────────────┘
```

## Design Decisions

### 1. pgvector over managed vector DBs
Using pgvector keeps the stack simple (one database) and avoids vendor lock-in. The `Retriever` base class in `src/retrieval/base.py` makes it swappable if needed.

### 2. Swappable retriever interface
`src/retrieval/base.py` defines an abstract `Retriever` so the underlying store (pgvector, Pinecone, Weaviate) can be swapped without changing agent code.

### 3. Governance as a separate layer
Guardrails (PII detection, topic filtering, audit logging) live in `src/governance/` and are applied by the supervisor — not baked into the agent. This keeps the agent logic clean and the governance layer independently testable.

### 4. Resumable ingest pipeline
`src/ingest/pipeline.py` tracks progress so large ingest jobs can be interrupted and resumed without re-embedding already-processed records.

### 5. Synthetic data (Synthea)
Patient data is generated via Synthea or `generate_data.py` — no real PHI ever enters the system.

### 6. Separation of config
All environment variables, model IDs, and region settings are loaded in `src/config.py` as the single source of truth. No hardcoded values elsewhere.
