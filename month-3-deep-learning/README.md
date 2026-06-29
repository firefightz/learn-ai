# Month 3 — Deep Learning & Neural Networks

**Goal:** Build and train neural networks with a real framework (**PyTorch**). You'll
move from "I use models" to "I train models," still working by intuition — the
training math gets formalized in Month 5.

---

## Week 1 — What a Neural Network Is (and Tensors)
**Objectives:** Understand a network's building blocks and PyTorch's core object.

**Topics**
- Neuron → layer → network; weights, activations, "depth."
- Why deep learning beat classic ML on images/text.
- Tensors: the array type everything runs on; shapes, devices (CPU/GPU).
- The training loop conceptually: forward → loss → backward → update.

**Hands-on lab**
- Tensor warm-up in PyTorch. Then hand-write a training loop for a tiny network on
  toy data and watch the loss go down.

**Deliverable:** `labs/week1-tensors-and-loop.ipynb`.

---

## Week 2 — Training an Image Classifier
**Objectives:** Build, train, and evaluate a real network end-to-end.

**Topics**
- `nn.Module`: defining a model. Layers, activations, the forward pass.
- Loss functions and optimizers (`SGD`, `Adam`) — what they do for you.
- Epochs, batches, learning rate; overfitting and how you spot it.
- Convolution at a high level — why it suits images.

**Hands-on lab**
- Train a classifier on MNIST or CIFAR-10. Plot training/validation curves.
  Tweak the learning rate and see what happens.

**Deliverable:** `labs/week2-image-classifier.ipynb`.

---

## Week 3 — Sequences & Text
**Objectives:** Apply neural nets to sequential data and connect to LLMs.

**Topics**
- Representing text for a network: embeddings revisited.
- Sequence models (RNN/LSTM idea) and where transformers improved on them.
- The transformer at an intuition level — attention as "what should I look at."
- Connecting back to Month 1: this is what powers the LLMs you used.

**Hands-on lab**
- Train a simple text classifier (sentiment) or a tiny character-level model that
  generates text. Watch it learn structure.

**Deliverable:** `labs/week3-text-model.ipynb`.

---

## Week 4 — Project Week
**Objectives:** Own a full deep-learning project and explain what the model learned.

**Hands-on lab → Project**
See [`projects/month-3-project.md`](./projects/month-3-project.md).

**Deliverable:** A trained network + a write-up of architecture, results, and what
it actually learned.

---

## Resources
- The official PyTorch "60-Minute Blitz" and "Learn the Basics" tutorials.
- A transformer explainer (illustrated/visual) for intuition.
- Repo-level [`resources.md`](../resources.md).
