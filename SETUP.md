# Environment Setup (one time)

You're comfortable in Python, so this is quick.

## 1. Python & a virtual environment
Use Python 3.11+.

```bash
python3 -m venv .venv
source .venv/bin/activate        # macOS/Linux
pip install --upgrade pip
```

## 2. Core libraries (install as you reach the month that needs them)
Install everything at once:

```bash
pip install -r requirements.txt
```

Or install only what you need for the current month:

```bash
# Month 1 — building with LLMs
pip install anthropic python-dotenv jupyter

# Month 2 — classic ML
pip install numpy pandas scikit-learn matplotlib seaborn

# Month 3 — deep learning
pip install torch torchvision

# Month 4 — agents, RAG, serving
pip install anthropic chromadb pypdf fastapi uvicorn requests

# Month 5 — math & data science (mostly already installed)
pip install scipy statsmodels
```

## 3. Models: Claude + Ollama
Month 1 onward uses two providers:

- **Claude (Anthropic API):** the capable model, for quality, planning, and final answers.
- **Ollama (local, free):** for cheap, high-volume iteration and embeddings.

**Claude**
1. Create an API key at console.anthropic.com. API usage is billed separately from a Claude.ai subscription.
2. Store it in a local `.env` file (already git-ignored). Start from [`.env.example`](./.env.example):

```
ANTHROPIC_API_KEY=sk-ant-...
```

**Ollama** (MacBook Pro M4 Pro, 24GB: keep models at about 14GB or less)
```bash
brew install ollama        # or the app from ollama.com
ollama pull gpt-oss:20b    # main local model
ollama pull qwen3:8b       # fast, cheap steps
ollama pull nomic-embed-text   # embeddings (Month 4 RAG)
curl http://localhost:11434    # should print "Ollama is running"
```

**Use both through one helper.** [`common/llm.py`](./common/llm.py) keeps the provider
code in one place, so every lab can switch with one argument. Run scripts from the
repo root so `common` is importable:

```python
from common.llm import ask, embed
ask("Explain tokens in two lines", provider="ollama")
ask("Explain tokens in two lines", provider="claude")
```

> **Never commit `.env` or API keys.** The `.gitignore` in this repo excludes it.

## 4. Notebooks
Most labs run great in Jupyter:
```bash
jupyter lab
```
