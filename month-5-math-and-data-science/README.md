# Month 5 — The Math & Data Science Backbone

**Goal:** Now that you've *built* everything, learn the theory that explains it. Every
topic here connects back to something you already made in Months 1–4 — that's why
it sticks.

This is the "why" month. We keep it hands-on (in the style of an applied
data-science course): you'll implement the math in code, not just read it.

---

## Week 1 — Linear Algebra (the shape of AI)
**Objectives:** See that embeddings and neural layers *are* linear algebra.

**Topics**
- Vectors and vector spaces; what an embedding really is.
- Dot products & cosine similarity → *this is your Month-4 semantic search*.
- Matrices and matrix multiplication → *this is a neural-network layer*.
- Norms and distance.

**Hands-on lab**
- In NumPy: implement cosine similarity from scratch, re-create your Week-4 semantic
  search with raw matrix math, and verify it matches the library version.

**Deliverable:** `labs/week1-linear-algebra.ipynb`.

---

## Week 2 — Calculus (how models learn)
**Objectives:** Understand gradient descent — the engine under all training.

**Topics**
- Derivatives and slopes; what "gradient" means.
- The chain rule → *this is backpropagation from Month 3*.
- Gradient descent: following the slope downhill.
- Learning rate, intuitively *and* now mathematically.

**Hands-on lab**
- Implement gradient descent by hand to fit a line — no ML library. Then connect it
  to the optimizer you used in PyTorch.

**Deliverable:** `labs/week2-gradient-descent.ipynb`.

---

## Week 3 — Probability & Statistics (what the model predicts)
**Objectives:** Read the world the way a model does — in distributions.

**Topics**
- Probability basics; distributions (normal, etc.).
- Mean, variance, standard deviation — and what they tell you about data.
- Bayes' theorem and conditional probability.
- Likelihood and why "next-token prediction" is a probability statement.
- Statistical significance & common pitfalls (p-values, correlation ≠ causation).

**Hands-on lab**
- With SciPy/statsmodels: explore distributions, run a hypothesis test, and compute
  a model's predicted-class probabilities — tie it back to temperature from Month 1.

**Deliverable:** `labs/week3-probability-stats.ipynb`.

---

## Week 4 — Data Science Craft + Capstone
**Objectives:** Master the data pipeline that underlies everything, and tie it all
together.

**Topics**
- pandas in depth: cleaning, joining, grouping, reshaping.
- Exploratory data analysis (EDA) and visualization (matplotlib/seaborn).
- The honest data-science workflow: question → data → clean → analyze → communicate.
- Feature engineering — and how good data beats fancy models.

**Hands-on lab → Capstone**
See [`projects/month-5-capstone.md`](./projects/month-5-capstone.md).

**Deliverable:** A capstone that uses the math and DS craft to revisit and improve
one of your earlier projects.

---

## Resources
- An applied stats/probability resource (e.g. Khan Academy for gaps, plus a
  hands-on data-science course in the style of your reference Udemy course).
- 3Blue1Brown's "Essence of Linear Algebra" and "Essence of Calculus" for intuition.
- pandas & seaborn official tutorials.
- Repo-level [`resources.md`](../resources.md).
