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
```bash
# Month 1 — building with LLMs
pip install anthropic python-dotenv jupyter

# Month 2 — classic ML
pip install numpy pandas scikit-learn matplotlib seaborn

# Month 3 — deep learning
pip install torch torchvision

# Month 4 — agents, RAG, serving
pip install anthropic chromadb fastapi uvicorn requests

# Month 5 — math & data science (mostly already installed)
pip install scipy statsmodels
```

## 3. API access
Month 1 onward uses the **Claude API** (latest models — default to the most capable
Claude model available, e.g. Opus, for quality; use a smaller one like Haiku for
cheap/fast iteration).

1. Get an API key from the Anthropic Console.
2. Store it in a local `.env` file (already git-ignored):

```
ANTHROPIC_API_KEY=sk-ant-...
```

```python
# load it in code
from dotenv import load_dotenv
load_dotenv()
```

> **Never commit `.env` or API keys.** The `.gitignore` in this repo excludes it.

## 4. Notebooks
Most labs run great in Jupyter:
```bash
jupyter lab
```
