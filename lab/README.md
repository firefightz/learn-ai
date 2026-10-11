# Hands-on Lab: Local + Cloud AI Stack

The build-it track that runs alongside the course. Each module has a checklist, starter code, and a "done when" line.

**Machine:** MacBook Pro M4 Pro, 24GB unified memory. Keep local models at about 14GB or less.
**Runtime:** Ollama on `localhost:11434`. Main model `gpt-oss:20b`, plus `qwen3:8b` and `qwen3:14b`.
**Cloud:** Anthropic API (Opus for hard reasoning) and AWS `us-east-1`.

| # | Module | What you learn | Course link |
|---|--------|----------------|-------------|
| 00 | [setup](00-setup/) | Mac tooling, Python env, API keys | Month 1 |
| 01 | [local-llm](01-local-llm/) | Ollama, models, the local API | Month 1 |
| 02 | [litellm-router](02-litellm-router/) | Route cheap work to local models, hard work to Opus | Month 4 |
| 03 | [mcp-local](03-mcp-local/) | Python MCP server for files and Gmail, read/draft only | Month 4 W3 |
| 04 | [mcp-aws](04-mcp-aws/) | Cloud notes MCP server on AWS (DynamoDB) | Month 4 W4 |
| 05 | [opencode-agent](05-opencode-agent/) | Agent harness pointed at local models | Month 4 W3–4 |
| 06 | [rag-local](06-rag-local/) | RAG from scratch: chunk, embed, Chroma, answer | Month 4 W1–2 |
| 07 | [rag-aws](07-rag-aws/) | The same RAG pipeline, rebuilt on AWS | Month 4 W2 |
| 08 | [github-actions](08-github-actions/) | AI pipelines as scheduled workflows | Any |

Install the lab extras with `pip install -r lab/requirements.txt`.

Log each session in [`log.md`](log.md). Record what broke in [`experiments/failures.md`](experiments/failures.md).
