# Month 1 — Foundations & the Modern Landscape

**Goal:** Understand what modern AI actually is, and start building with it
immediately. By Week 4 you'll have shipped a working LLM-powered app.

No math yet. We build mental models, then build software.

---

## Week 1 — The Field Map
**Objectives:** Place every buzzword on a single map so nothing later feels foreign.

**Topics**
- AI vs. Machine Learning vs. Deep Learning vs. Generative AI — the nested circles.
- A short history: rules → statistics → neural nets → transformers → today.
- Where LLMs, agents, RAG, computer vision, and diffusion fit.
- The core vocabulary: model, training, inference, parameters, dataset.

**Hands-on lab**
- Draw the field map yourself (diagram or markdown). For each term, write one
  sentence in your own words and one real product that uses it.

**Deliverable:** `notes/week1-field-map.md` — your one-page map.

---

## Week 2 — How LLMs Actually Work (Conceptually)
**Objectives:** Build an accurate mental model of an LLM without any math.

**Topics**
- Tokens: how text becomes numbers the model sees.
- Next-token prediction — the whole game in one idea.
- Training vs. inference; what "weights" are.
- Context window, temperature, and why models hallucinate.

**Hands-on lab**
- Use a tokenizer (e.g. `tiktoken`) to tokenize a paragraph.
  Count tokens, see how rare words split, observe how whitespace/casing matter.

**Deliverable:** `notes/week2-llm-explainer.md` — explain "how an LLM answers a
question" to a smart friend, plus your token experiment output.

---

## Week 3 — Prompting & Working with Models
**Objectives:** Get reliable, structured behavior out of a model.

**Topics**
- Anatomy of a prompt: system vs. user; role and instructions.
- Techniques: few-shot examples, step-by-step, output formatting.
- Structured output (JSON) and why it matters for real apps.
- Limits: hallucination, context limits, when *not* to use an LLM.

**Hands-on lab**
- Build a small **prompt library**: 5 reusable prompts (summarize, classify,
  extract, rewrite, brainstorm). Make one return strict JSON and parse it in Python.

**Deliverable:** `notes/week3-prompt-library.md` + a script that calls one prompt
and parses structured output.

---

## Week 4 — First Builds (Project Week)
**Objectives:** Call the OpenAI API from Python and ship something real.

**Topics**
- The OpenAI Python SDK: messages, system/developer prompts, model choice,
  streaming.
- Managing API keys safely (`.env`).
- Cost & model selection: capable model for quality, small model for speed/cost.
- Basic error handling and retries.

**Hands-on lab → Project**
See [`projects/month-1-project.md`](./projects/month-1-project.md).

**Deliverable:** A working **CLI summarizer or chatbot** that takes input, calls the
OpenAI API, and prints a useful response. Committed to `projects/`.

---

## Resources
- OpenAI API docs & the Python SDK quickstart.
- Your reference agentic-AI course — Month 1 maps to its "intro / first API calls" units.
- See repo-level [`resources.md`](../resources.md).
