from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Sample documents
documents = [
    "The cat sat on the mat.",
    "The dog barked at the mailman.",
    "The quick brown fox jumps over the lazy dog.",
    "Embeddings are used to represent text numerically."
]

# Initialize embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Generate embeddings for documents
document_embeddings = model.encode(documents)

# Sample query
query = "What does the fox do?"

# Generate embedding for the query
query_embedding = model.encode(query)

# Calculate cosine similarity between query and documents
similarities = cosine_similarity([query_embedding], document_embeddings)[0]

# Find the most similar document (index)
most_similar_index = np.argmax(similarities)

# Retrieve the most similar document
retrieved_document = documents[most_similar_index]

print(f"Query: {query}")
print(f"Retrieved Document: {retrieved_document}")
print(f"Similarity Score: {similarities[most_similar_index]}")