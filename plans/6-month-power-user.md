# 6-Month AI Plan: 30 min/day

**Goal:** become the AI power user at work. **Level:** professional developer who already orchestrates agents, so this plan has no beginner content.
**Budget:** 30 min/day, about 5 days/week, roughly 65 hours total.

## Each session
- **20 min:** do the thing. Read, run, break something.
- **10 min:** write it down in your own words. If time is short, cut the 20, not the 10.
- **Mon–Thu:** new material. **Fri:** apply it at work. **Monday:** plan the week's material in bulk, so you never hunt for it mid-session.

## Month 1: A mental model that predicts behavior
- W1: Tokens, tokenization, context windows
- W2: Next-token prediction, sampling, temperature/top-p
- W3: Training stages: pretraining, fine-tuning, RLHF, and why models hedge or hallucinate
- W4: Context engineering: position effects, context rot, what to include vs. retrieve vs. leave out
- **Deliverable:** `notes/why-models-fail.md`, with 10 failure modes you reproduced yourself

## Month 2: Agentic coding, done deliberately
- W1: Context files (`CLAUDE.md` / `AGENTS.md`): what belongs in them and what bloats them
- W2: Subagents and delegation; choosing a model per task
- W3: MCP and tool design: write one server (→ `lab/03-mcp-local`)
- W4: Permissions, sandboxing, blast radius
- **Deliverable:** `playbooks/agent-setup.md`, your standard config for a new repo

## Month 3: Retrieval and grounding
- W1: Embeddings and vector similarity: semantic search over your own notes
- W2: Chunking, metadata filters, hybrid search, reranking
- W3: RAG failure modes: bad retrieval, right chunk with wrong answer, stale index
- W4: Deciding between long context, RAG, fine-tuning, and a better prompt
- **Deliverable:** working search over this repo (→ `lab/06-rag-local`)

## Month 4: The API directly
- W1: Raw calls, streaming, system prompts, message history
- W2: Structured outputs: schemas, validation, retries
- W3: Write a tool-use loop by hand
- W4: Cost and latency: caching, batching, model tiering (→ `lab/02-litellm-router`)
- **Deliverable:** one small internal tool that does something real at work

## Month 5: Evals and reliability (the differentiator)
- W1: An eval set of 20–50 real examples
- W2: Grading: exact match, rubrics, LLM-as-judge and its biases
- W3: Regression tests for prompt changes and model upgrades
- W4: Guardrails, fallbacks, human-in-the-loop, prompt injection basics
- **Deliverable:** an eval suite for the Month 4 tool, with a before/after number

## Month 6: Leverage across the org
- W1: Find the 5 highest-value repetitive tasks on your team
- W2: Data handling and privacy; your company's actual policy
- W3: Turn 3 playbooks into guides a non-engineer can follow
- W4: A reading routine you can sustain at 30 min/week
- **Deliverable:** an internal doc or a short talk

## When you fall behind
- Missed days: skip ahead and don't backfill.
- Missed a week: drop that topic.
- Missed a month: do only the monthly deliverable, then continue.
