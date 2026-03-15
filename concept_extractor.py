import spacy

nlp = spacy.load("en_core_web_sm")

def extract_concepts(text, top_n=10):
    doc = nlp(text)
    # Extract noun chunks as candidate concepts, limit to 3 words
    chunks = [chunk.text for chunk in doc.noun_chunks if len(chunk.text.split()) <= 3]
    # Remove duplicates and return top_n
    unique_chunks = list(dict.fromkeys(chunks))
    return unique_chunks[:top_n]
