import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample knowledge base (documents)
documents = [
    
    "Artificial Intelligence enables machines to learn.",
    "Retrieval-Augmented Generation (RAG) combines retrieval and generation.",
    #"Machine learning is a subset of AI.",
    "Machine learning is a subset of AI in world of Machine learning.",
    "America is a country in North America.",
    #"America is a finalicially developed country.",
    "Chine is in Asia.",
    "The capital of France is Paris.",
    "Python is a popular programming language."
]

# Simple retrieval function using TF-IDF
def retrieve(query, docs, top_k=4):
    vectorizer = TfidfVectorizer()
    doc_vectors = vectorizer.fit_transform(docs + [query])
    query_vec = doc_vectors[-1]
    doc_vecs = doc_vectors[:-1]
    similarities = cosine_similarity(query_vec, doc_vecs).flatten()
    top_indices = similarities.argsort()[-top_k:][::-1]
    return [docs[i] for i in top_indices]

# Simple generation function (concatenates retrieved docs and query)
def generate_answer(query, retrieved_docs):
    context = " ".join(retrieved_docs)
    return f"Context: {context}\nQuestion: {query}\nAnswer: [Your answer here]"

# Example usage
if __name__ == "__main__":
    user_query = "What America?"
    retrieved = retrieve(user_query, documents)
    answer = generate_answer(user_query, retrieved)
    print(answer)