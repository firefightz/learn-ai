# Month 2 — Machine Learning, Applied

**Goal:** Train, evaluate, and ship machine-learning models with **scikit-learn** —
building intuition through experiments before you meet the math in Month 5.

This month mirrors a hands-on, applied data-science course: load data, train a
model, measure it, repeat. You feel the concepts before you formalize them.

---

## Week 1 — The ML Mindset & Your First Classifier
**Objectives:** Understand the supervised-learning loop and train a real classifier.

**Topics**
- Supervised vs. unsupervised vs. reinforcement learning — what each is *for*.
- Features, labels, training data, predictions.
- The workflow: split → train → predict → evaluate.
- Train/test split and *why* you never evaluate on training data.

**Hands-on lab**
- Load a classic dataset (iris, wine, or titanic). Train a classifier
  (`LogisticRegression` or `DecisionTree`). Report accuracy on a held-out test set.

**Deliverable:** `labs/week1-first-classifier.ipynb`.

---

## Week 2 — Regression & Predicting Numbers
**Objectives:** Predict continuous values and read regression metrics.

**Topics**
- Regression vs. classification.
- Linear regression intuition (the line of best fit — math comes in Month 5).
- Metrics: MAE, RMSE, R² — what "good" looks like.
- Feature scaling and basic preprocessing with pandas.

**Hands-on lab**
- Predict house prices or similar. Compare two models. Plot predicted vs. actual.

**Deliverable:** `labs/week2-regression.ipynb` with a short metrics write-up.

---

## Week 3 — Unsupervised Learning & Finding Structure
**Objectives:** Discover patterns when there are no labels.

**Topics**
- Clustering (k-means) and what the clusters mean.
- Dimensionality reduction at a high level (PCA — the intuition, math later).
- Overfitting vs. underfitting; the bias–variance idea, felt not derived.
- Cross-validation for trustworthy scores.

**Hands-on lab**
- Cluster a dataset (e.g. customers or iris without labels). Visualize the clusters.
  Use cross-validation on a supervised model and compare to a single split.

**Deliverable:** `labs/week3-clustering.ipynb`.

---

## Week 4 — End-to-End Project
**Objectives:** Run the full ML pipeline yourself and report results honestly.

**Hands-on lab → Project**
See [`projects/month-2-project.md`](./projects/month-2-project.md).

**Deliverable:** A complete predictor: data → cleaning → model → evaluation report.

---

## Resources
- scikit-learn user guide (the "Getting Started" and "Supervised learning" sections).
- A Kaggle "Intro to Machine Learning" track for extra practice datasets.
- Repo-level [`resources.md`](../resources.md).
