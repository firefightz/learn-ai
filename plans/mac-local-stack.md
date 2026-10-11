# Mac Local AI Stack Plan

Originally a weekend plan built around a PC with an RX 9070 XT. It now runs on the **MacBook Pro M4 Pro (24GB)** only. Work through it in about 1-hour sessions; each step has a checklist module in [`/lab`](../lab/).

## Hardware rules
- macOS lets the GPU use about 16–18GB, so keep models at **≤ ~14GB**.
- Expect roughly 20–40 tok/s on mid-size models.
- Don't run the chat model, the embedding model, and Docker apps all at once. Skip Docker and Open WebUI.

## Runtime and models
- **Ollama** is the default: most tutorials, LiteLLM, and MCP examples assume it. Keep it updated for the Apple Silicon (MLX) path.
- Add **LM Studio** later if you want a GUI or extra MLX speed. Don't load the same model in both at once.

| Model | Size | Use |
|---|---|---|
| `gpt-oss:20b` | ~13GB | Main reasoning and tool calling |
| `qwen3:14b` | ~9GB | All-rounder with room for long context |
| `qwen3:8b` | ~5GB | Fast: routing, summaries, cheap agent steps |
| `nomic-embed-text` | small | Embeddings for RAG |

Skip dense 27–32B models: they crowd out context and run slowly on 24GB.

## Order
1. **Local LLM server.** Ollama plus the models above. → `lab/01`
2. **LiteLLM router.** Local for cheap work, Opus over the API for hard reasoning. → `lab/02`
3. **Local MCP server.** Files and Gmail, read/draft only, no send, bound to `127.0.0.1`. → `lab/03`
4. **AWS cloud notes MCP server.** DynamoDB, a $15 budget alarm, and an IAM role (never your own keys). → `lab/04`
5. **OpenCode agent harness.** Pointed at `localhost:11434`. → `lab/05`
6. **RAG from scratch, locally.** Chroma, `pypdf`, `nomic-embed-text`. → `lab/06`
7. **AWS DIY RAG** (by hand, not Bedrock Knowledge Bases). → `lab/07`
8. **GitHub Actions AI pipeline.** The scheduled "AI article of the day" job. → `lab/08`

## Dropped from the PC version
The PC setup, Tailscale, Wake-on-LAN, `OLLAMA_HOST=0.0.0.0`, firewall rules, and Windows auto sign-in.

## Detailed guides (Claude Docs)
- [Build an MCP Server on AWS for Your Local LLM](https://claude.ai/code/artifact/7b7cfd4d-464b-468e-94ab-394b3c3aac47). Written for the PC; on the Mac, swap PC addresses for `localhost`.
- The RAG guide (local + AWS) is in your Claude Docs. It assumed the PC, but the steps are the same on the Mac.
