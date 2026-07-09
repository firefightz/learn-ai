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
pip install openai python-dotenv jupyter

# Month 2 — classic ML
pip install numpy pandas scikit-learn matplotlib seaborn

# Month 3 — deep learning
pip install torch torchvision

# Month 4 — agents, RAG, serving
pip install openai chromadb fastapi uvicorn requests

# Month 5 — math & data science (mostly already installed)
pip install scipy statsmodels
```

## 3. API access
Month 1 onward uses the **OpenAI API** with ChatGPT-style models. Default to a
capable model for quality; use a smaller model for cheap/fast iteration.

1. Get an API key from the OpenAI platform.
2. Store it in a local `.env` file (already git-ignored). You can start from
   [`.env.example`](./.env.example):

```
OPENAI_API_KEY=sk-...
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
