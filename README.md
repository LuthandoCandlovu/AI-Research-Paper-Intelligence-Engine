<div align="center">

<!-- Animated Header -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:4f8bff,100:a78bfa&height=200&section=header&text=AI%20Research%20Paper%20Intelligence%20Engine&fontSize=32&fontColor=ffffff&fontAlignY=38&desc=Upload%20PDFs.%20Discover%20Insights.%20Find%20Research%20Gaps.&descAlignY=58&descSize=16" width="100%"/>

<!-- Badges -->
<p>
  <img src="https://img.shields.io/badge/Python-3.9+-4f8bff?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/spaCy-09A3D5?style=for-the-badge&logo=spacy&logoColor=white"/>
  <img src="https://img.shields.io/badge/License-MIT-34d399?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Status-Active-34d399?style=for-the-badge"/>
</p>

<!-- One-liner -->
<p>
  <strong>An intelligent ML pipeline that transforms raw academic PDFs into a visual research landscape — revealing clusters, concepts, and unexplored gaps.</strong>
</p>

<br/>

<!-- Demo GIF placeholder -->
<img src="https://raw.githubusercontent.com/your-org/ai-research-engine/main/assets/demo.gif" width="75%" alt="Demo" style="border-radius:12px"/>

<br/><br/>

</div>

---

## ✨ Features

| Feature | Description |
|---|---|
| 📄 **PDF Extraction** | Parses academic papers and extracts clean text using PyMuPDF |
| 🧠 **Concept Extraction** | spaCy NLP pipeline identifies named entities and domain keywords |
| 🔢 **Semantic Embeddings** | Sentence-Transformers encode concepts into rich vector representations |
| 🗺️ **UMAP Projection** | Reduces high-dimensional embeddings to 2D for visualization |
| 🔵 **HDBSCAN Clustering** | Density-based clustering groups related research topics automatically |
| 🔭 **Gap Detection** | Identifies sparse cluster regions as unexplored research opportunities |
| ⚡ **Streamlit UI** | Interactive, no-code interface for uploading papers and exploring results |

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        📥  INPUT LAYER                          │
│                                                                   │
│   PDF Upload  ──►  Text Extractor  ──►  Preprocessor            │
│  (Streamlit)      (PyMuPDF)            (spaCy tokenizer)        │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                     🧠  INTELLIGENCE LAYER                       │
│                                                                   │
│   spaCy NLP  ──►  Sentence-Transformers  ──►  UMAP              │
│  (NER + POS)      (384-dim embeddings)       (2D projection)    │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                       🎯  OUTPUT LAYER                          │
│                                                                   │
│   HDBSCAN  ──►  Gap Analyser  ──►  Streamlit Visualisation      │
│ (clustering)   (opportunity)      (interactive charts)          │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🚀 Installation

> **Requirements:** Python 3.9+, pip

### 1 — Clone the repository

```bash
git clone https://github.com/your-org/ai-research-engine.git
cd ai-research-engine
```

### 2 — Create a virtual environment

```bash
python -m venv venv
```

### 3 — Activate the environment

```bash
# Windows
.\venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 4 — Install dependencies

```bash
pip install -r requirements.txt
```

### 5 — Launch the app 🎉

```bash
streamlit run app.py
```

The app opens automatically at `http://localhost:8501`

---

## 📖 Usage

```
1.  Open the app in your browser
2.  Upload at least 3 PDF research papers
3.  The pipeline runs automatically:
      • Extracts text from each PDF
      • Identifies key concepts with spaCy
      • Encodes concepts with Sentence-Transformers
      • Projects embeddings to 2D with UMAP
      • Clusters topics with HDBSCAN
4.  Explore the interactive cluster map
5.  Review suggested research gaps highlighted in the gap panel
```

> 💡 **Tip:** Upload papers from the same domain for tighter, more meaningful clusters. Upload across domains to discover interdisciplinary bridges.

---

## 🛠️ Tech Stack

<div align="center">

| Layer | Technology | Role |
|---|---|---|
| PDF parsing | `PyMuPDF` | Fast, accurate text extraction |
| NLP | `spaCy` | Named entity recognition, tokenisation |
| Embeddings | `sentence-transformers` | Semantic vector encoding |
| Dimensionality reduction | `umap-learn` | 2D/3D projection |
| Clustering | `hdbscan` | Density-based topic grouping |
| Visualisation | `Plotly` | Interactive cluster charts |
| Data handling | `NumPy` + `Pandas` | Array ops and data frames |
| UI | `Streamlit` | No-code interactive interface |

</div>

---

## 📁 Project Structure

```
ai-research-engine/
├── app.py                  # Streamlit entry point
├── requirements.txt        # Python dependencies
├── README.md
│
├── pipeline/
│   ├── extractor.py        # PDF → raw text
│   ├── nlp.py              # spaCy concept extraction
│   ├── embedder.py         # Sentence-Transformer encoding
│   ├── reducer.py          # UMAP projection
│   └── clusterer.py        # HDBSCAN + gap detection
│
├── ui/
│   ├── components.py       # Reusable Streamlit widgets
│   └── charts.py           # Plotly visualisation helpers
│
└── assets/
    └── demo.gif
```

---

## 🗺️ Roadmap

- [x] PDF text extraction
- [x] spaCy concept extraction
- [x] Sentence-Transformer embeddings
- [x] UMAP + HDBSCAN clustering
- [x] Streamlit UI
- [ ] 3D cluster visualisation
- [ ] Export cluster report to PDF
- [ ] GPT-powered gap explanation
- [ ] Citation network analysis
- [ ] Multi-language paper support

---

## 🤝 Contributing

Contributions are welcome! Here's how:

```bash
# 1. Fork the repo and clone your fork
git clone https://github.com/YOUR-USERNAME/ai-research-engine.git

# 2. Create a feature branch
git checkout -b feature/my-new-feature

# 3. Commit your changes
git commit -m "feat: add my new feature"

# 4. Push and open a Pull Request
git push origin feature/my-new-feature
```

Please follow [Conventional Commits](https://www.conventionalcommits.org/) for commit messages.

---

## 📄 License

This project is licensed under the **MIT License** — see [`LICENSE`](LICENSE) for details.

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:a78bfa,100:4f8bff&height=120&section=footer" width="100%"/>

<p>Made with ❤️ using spaCy · Sentence-Transformers · HDBSCAN · Streamlit</p>

</div>
