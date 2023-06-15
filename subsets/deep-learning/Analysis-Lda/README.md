# Topic Analysis of Review Data (Lenovo K8) 

This project analyzes Amazon India reviews for the Lenovo K8 budget smartphone to understand the **Voice of the Customer (VOC)**. We use **syntactic processing (POS tagging)** and **topic modeling (LDA)** to identify the main aspects customers talk about (battery, camera, network, performance, etc.) and summarize them in a business-friendly format.

---

## Objective

* Discover key topics customers discuss in Lenovo K8 reviews
* Focus on **product aspects** by restricting tokens to **nouns**
* Build **LDA topic models**, evaluate topic quality, and select an optimal number of topics
* Provide **business-friendly topic names** and a final **topic table** for stakeholders

---

## Dataset

**File:** `K8 Reviews v0.2.csv`
**Columns:**

* `sentiment` — binary sentiment label derived from ratings (positive vs negative)
* `review` — customer review text

---

## Workflow

### 1) Text Preprocessing

* **Lowercasing**: normalize casing across reviews
* **Tokenization**: split text into tokens
* **POS Tagging (NLTK)**: tag each token with part-of-speech
* **Noun-only filtering**: keep only tokens corresponding to nouns
  **Noun tags used:** `NN`, `NNS`, `NNP`, `NNPS`
* **Stopword + punctuation removal**: reduce noise
* **Lemmatization**: normalize word forms (e.g., *cameras → camera*)

### 2) Topic Modeling (LDA)

* Train a baseline **LDA model with 12 topics** (as required)
* Print **top terms per topic** for interpretation

### 3) Coherence / Model Quality

* Evaluate the model using a coherence approach
  *(If standard `gensim` c_v coherence is not available due to environment constraints, a co-occurrence based coherence proxy can be used for stable topic selection.)*

### 4) Optimal Topic Count

* Train LDA models over a range of topic counts (e.g., `k = 4 … 20`)
* Select `best_k` based on the highest coherence score while keeping topics interpretable
* Train a final LDA model with `best_k`

---

## Results Summary (Business Lens)

Common themes typically found in Lenovo K8 customer reviews include:

* **Battery & Charging** (battery life, charging speed, usage time)
* **Camera & Photo Quality** (camera, picture, quality)
* **Network / SIM / Signal** (network, sim, signal, connectivity)
* **Screen & Build Quality** (screen, glass, device)
* **Performance & Software** (performance, apps, updates, bugs)
* **Price & Value for Money** (price, budget, worth, value)
* **Purchase / Delivery / Support** (delivery, Amazon, service, return-related terms)

### Topic Consolidation

Some topics may overlap and can be merged to improve stakeholder readability, for example:

* multiple battery-related topics → **Battery & Charging**
* multiple camera-related topics → **Camera & Photo Quality**
* multiple general experience topics → **Overall Experience / Features**

---

## Deliverables

* Baseline LDA (**12 topics**) + top terms per topic
* Coherence score for baseline model
* Optimal-topic LDA (**best_k**) + coherence score
* Final business table with:

  * **Topic Name**
  * **Top 10 Terms** per topic

---

## How to Run

1. Place `K8 Reviews v0.2.csv` in the same folder as the notebook.
2. Run the notebook cells in order:

   * load data
   * preprocess text (POS + nouns-only)
   * train baseline LDA (12 topics)
   * compute coherence + select best_k
   * train final model
   * generate topic names + final table

---

## Author

Developed by Gresa Hisa (@gresium) — AI & Cybersecurity Engineer | AI & Machine Learning Specialist
GitHub: https://github.com/gresium

