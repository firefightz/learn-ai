# Month 4 Project — Ship an Agentic AI Application

Combine the month's pieces into one deployed application.

## Build one
1. **Document assistant** — RAG over a document set, served via an API, that answers
   with citations.
2. **Task agent** — an agent with several tools that completes a real multi-step task
   (research-and-summarize, data lookup + computation, etc.).
3. **Hybrid** — an agent that *also* retrieves from a knowledge base when it needs facts.

## Requirements
- A working **agent loop** or **RAG pipeline** (ideally both).
- At least one real **tool** the model can call (or real retrieval).
- Served behind a **FastAPI** endpoint you can `curl` or hit from a browser.
- Sensible **guardrails**: stopping conditions, input validation, error handling.
- API keys from `.env`; nothing secret committed.
- `README.md`: what it does, architecture sketch, how to run and call it.

## Stretch goals
- Basic logging of each agent step for debugging.
- A tiny eval set: 5–10 questions/tasks and whether the system handles them.
- A minimal web UI.

## Done when
You can start the server, hit the endpoint, and watch your system reason, use a
tool or retrieve context, and return a grounded answer.
