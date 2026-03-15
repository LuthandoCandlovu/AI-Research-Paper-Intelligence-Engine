# AI Research Paper Intelligence Engine

Upload PDFs, extract concepts, cluster research topics, and suggest future research gaps.

## Features
- PDF text extraction
- Key concept extraction (spaCy)
- Semantic embeddings (Sentence‑Transformers)
- Clustering (HDBSCAN + UMAP)
- Streamlit UI

## Installation
1. Clone the repo
2. Create virtual environment: `python -m venv venv`
3. Activate: `.\venv\Scripts\activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run: `streamlit run app.py`

## Usage
Upload at least 3 PDFs to see clustering in action.
