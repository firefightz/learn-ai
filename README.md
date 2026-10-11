# Learn AI — A 5-Month Hands-On Course

A self-paced course to learn AI from the **top down**: you build and use real AI
systems first, develop intuition for *what* the pieces do, and only at the end go
under the hood to the **math and data science** that explain *why* they work.

This structure is deliberate. Most courses front-load months of math and lose you
before you build anything. Here you'll ship working AI in Week 4 and understand the
mathematics underneath it by the time you finish — when you have real hooks to hang
it on.

## Who this is for
- Comfortable in Python (no language ramp-up included).
- Wants **practical, build-it** lessons over passive theory.
- Inspired in flavor by hands-on agentic-AI engineering and applied data-science courses.

## The 5-month arc

| Month | Theme | What you'll be able to do |
|-------|-------|---------------------------|
| 1 | [Foundations & the Modern Landscape](./month-1-foundations/) | Explain how modern AI works; build your first LLM-powered app |
| 2 | [Machine Learning, Applied](./month-2-machine-learning/) | Train, evaluate, and ship ML models with scikit-learn |
| 3 | [Deep Learning & Neural Networks](./month-3-deep-learning/) | Build and train neural nets in PyTorch |
| 4 | [Specializations & Agentic Systems](./month-4-specializations-agents/) | Build RAG, tools, and multi-step AI agents; deploy them |
| 5 | [The Math & Data Science Backbone](./month-5-math-and-data-science/) | Understand the linear algebra, calculus, probability, and DS craft under it all |

## Other plans and the hands-on lab
- [`plans/`](./plans/): all my learning plans (this course, the 6-month power-user plan, and the Mac local AI stack) and how they overlap.
- [`lab/`](./lab/): build-it modules for my MacBook (Ollama, LiteLLM, MCP, agents, RAG local + AWS, GitHub Actions).

**Models:** everything uses **Claude** (API) and **Ollama** (local on the Mac). Both go through [`common/llm.py`](./common/llm.py); see [`SETUP.md`](./SETUP.md).

## How to use this repo
- Each month is a folder with a `README.md` giving the **weekly breakdown**:
  objectives, topics, a **hands-on lab**, a **deliverable**, and resources.
- Do the lab every week — the labs are the point. Reading is scaffolding.
- Each month ends in a **project** in its `projects/` folder. Build it; commit it.
- Put weekly written work in `notes/` and hands-on experiments in `labs/` inside
  the relevant month folder.
- Track progress in [`PROGRESS.md`](./PROGRESS.md).
- One-time environment setup: [`SETUP.md`](./SETUP.md).
- Curated links live in [`resources.md`](./resources.md).

## The one rule
**Build something every week.** If a week ends and you haven't run code that does
something, you skipped the most important part.
