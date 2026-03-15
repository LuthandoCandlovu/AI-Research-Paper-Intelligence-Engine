from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embedding(text):
    # If text is very long, you might truncate or chunk; for now full text
    return model.encode(text, convert_to_tensor=True)
