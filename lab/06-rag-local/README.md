# 06 · RAG from scratch (local)

Everything by hand so nothing is hidden: load → chunk → embed → store → retrieve → answer.

- [ ] `ollama pull nomic-embed-text` · `uv pip install chromadb pypdf`
- [ ] Put a `.txt` and a `.pdf` in `docs/`
- [ ] `python ingest.py` — chunks, embeds, stores in `./chroma/`
- [ ] `python query.py "question"` — shows answer + which chunks it used
- [ ] Re-run ingest: unchanged files should be skipped (hash check)
- [ ] Break it on purpose: tiny chunks, huge chunks, no overlap. Log results in `experiments/failures.md`

**Done when:** you can explain why a right chunk can still give a wrong answer.
