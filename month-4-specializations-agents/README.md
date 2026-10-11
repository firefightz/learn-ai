# Month 4 — Specializations & Agentic Systems

**Goal:** Build the systems that define modern applied AI — embeddings, RAG, tools,
and **multi-step agents** — then serve one behind an API. This is the
agentic-engineering heart of the course.

This month leans hardest into "how to practically use things." Every week ships a
running system.

---

## Week 1 — Embeddings & Semantic Search
**Objectives:** Represent meaning as vectors and search by similarity.

**Topics**
- What an embedding is; meaning as geometry (preview of Month 5 linear algebra).
- Cosine similarity and nearest-neighbor search.
- Vector stores (e.g. Chroma) — what they do and why.
- Chunking text and why chunk size matters.

**Hands-on lab**
- Embed a folder of documents, store the vectors, and build a semantic search:
  type a query, get the most relevant chunks back.

**Deliverable:** `labs/week1-semantic-search/`.

---

## Week 2 — Retrieval-Augmented Generation (RAG)
**Objectives:** Make an LLM answer from *your* documents, with citations.

**Topics**
- The RAG pattern: retrieve relevant chunks → stuff into the prompt → generate.
- Grounding answers and reducing hallucination.
- Showing sources; handling "I don't know."
- Evaluating a RAG system: is the answer actually supported?

**Hands-on lab**
- Extend Week 1 into a Q&A app over your own docs. The model answers using retrieved
  context and cites which chunks it used.

**Deliverable:** `labs/week2-rag-qa/`.

---

## Week 3 — Tool Use & Agents
**Objectives:** Give a model tools and let it take multi-step actions.

**Topics**
- Function/tool calling: how the model requests an action and you run it.
- The agent loop: think → call tool → observe → repeat → answer.
- Designing good tools (clear names, schemas, narrow scope).
- Guardrails: stopping conditions, validation, cost/latency awareness.

**Hands-on lab**
- Build an agent with 2–3 tools (e.g. calculator, web/file lookup, your Month-2
  model as a tool). Watch it chain steps to solve a task.

**Deliverable:** `labs/week3-agent/`.

---

## Week 4 — Deploy: Serve an Agent (Project Week)
**Objectives:** Turn a notebook into a service, plus survey the rest of the landscape.

**Topics**
- Serving with FastAPI: an endpoint that runs your agent/RAG system.
- Basics of evaluation, logging, and monitoring for AI apps.
- Cost, latency, and model selection in production.
- **Landscape survey:** computer vision and generative/diffusion models — what they
  are and when you'd reach for them.

**Hands-on lab → Project**
See [`projects/month-4-project.md`](./projects/month-4-project.md).

**Deliverable:** A deployed AI application (agent or RAG) callable over HTTP.

---

## Resources
- Claude docs on tool use, structured outputs, and agents; Ollama docs on embeddings.
- Build these weeks in [`lab/`](../lab/): embeddings and RAG (`06`, `07`), tools via MCP (`03`, `04`), agents (`05`).
- Your reference agentic-AI engineering course — Month 4 is the closest match;
  pull its agent/RAG/deployment modules alongside these weeks.
- Repo-level [`resources.md`](../resources.md).
