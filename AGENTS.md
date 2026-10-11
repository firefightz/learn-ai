# Project Instructions

This repository is a hands-on AI learning course. Keep changes practical, concise,
and aligned with the existing monthly curriculum structure.

## Course Defaults
- LLM examples use **Claude** (Anthropic API) for capable/cloud work and **Ollama**
  (local, `http://localhost:11434`) for free/local work. Do not add OpenAI examples.
- Load `ANTHROPIC_API_KEY` from a local `.env` file. Ollama needs no key.
- Keep provider-specific code isolated in `common/llm.py` so labs can swap
  between Claude and Ollama with one argument.
- Target machine: MacBook Pro M4 Pro, 24GB. Keep local models at about 14GB or less
  (default `gpt-oss:20b`, fast `qwen3:8b`, embeddings `nomic-embed-text`).
- Avoid committing notebooks, data dumps, model artifacts, API keys, or personal data.

## Content Style
- Write in a direct, learner-facing voice.
- Keep each week focused on a concrete lab and a clear deliverable.
- When adding resources, prefer official docs and stable beginner-friendly references.
