import streamlit as st
import tempfile
import os
import numpy as np
from pdf_utils import extract_text_pdfplumber
from concept_extractor import extract_concepts
from embeddings import get_embedding
from clustering import cluster_papers

st.set_page_config(page_title="AI Research Paper Intelligence Engine", layout="wide")
st.title("📄 AI Research Paper Intelligence Engine")

uploaded_files = st.file_uploader("Upload PDFs", type="pdf", accept_multiple_files=True)

if uploaded_files:
    papers = []
    texts = []
    with st.spinner("Processing PDFs..."):
        for file in uploaded_files:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                tmp.write(file.read())
                tmp_path = tmp.name
            text = extract_text_pdfplumber(tmp_path)
            os.unlink(tmp_path)
            papers.append({"name": file.name, "text": text[:2000]})
            texts.append(text[:2000])
    
    # Generate embeddings
    embeddings = np.array([get_embedding(txt) for txt in texts])
    
    # Cluster
    labels = cluster_papers(embeddings)
    
    # Display results
    st.subheader("Clustering Results")
    for i, paper in enumerate(papers):
        st.write(f"**{paper['name']}** → Cluster {labels[i]}")
        concepts = extract_concepts(paper['text'])
        st.caption(f"Concepts: {', '.join(concepts)}")
    
    # Suggest gaps (basic)
    if len(set(labels)) > 1:
        st.subheader("Possible Research Gaps")
        st.info("Based on clustering, consider exploring intersections between clusters.")
