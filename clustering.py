import numpy as np
import umap
import hdbscan
import warnings

def cluster_papers(embeddings, min_cluster_size=3):
    n_samples = len(embeddings)
    
    # If we have too few samples, return all as noise or a single cluster
    if n_samples < min_cluster_size:
        warnings.warn(f"Only {n_samples} papers, minimum cluster size is {min_cluster_size}. Returning all as noise.")
        return np.full(n_samples, -1)  # -1 indicates noise
    
    # For very small datasets, skip UMAP (it needs at least ~10 points to work well)
    if n_samples < 10:
        # Use raw embeddings for clustering
        reduced_embeds = embeddings
    else:
        try:
            reducer = umap.UMAP(n_neighbors=min(15, n_samples-1), min_dist=0.1, metric='cosine')
            reduced_embeds = reducer.fit_transform(embeddings)
        except Exception as e:
            warnings.warn(f"UMAP failed: {e}. Falling back to raw embeddings.")
            reduced_embeds = embeddings
    
    # Cluster with HDBSCAN
    clusterer = hdbscan.HDBSCAN(min_cluster_size=min_cluster_size, metric='euclidean')
    labels = clusterer.fit_predict(reduced_embeds)
    return labels
