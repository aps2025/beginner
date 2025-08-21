
from langchain_community.embeddings import OllamaEmbeddings

from langchain.schema import Document
from langchain_core.vectorstores import InMemoryVectorStore


# Example documents for retrieval
documents = [
  {"page_content": "LangChain is a framework for developing applications powered by language models."},
  {"page_content": "LangChain provides components for prompt management, chains, and memory."},
  {"page_content": "You can use LangChain with local or cloud-based LLMs."}
]
docs = [Document(page_content=doc["page_content"]) for doc in documents]
embeddingOllama = OllamaEmbeddings(
    model="llama2"
)
text = "This is a sample document."
vectorstore = InMemoryVectorStore.from_texts([text], embedding=embeddingOllama)
vectorstore = InMemoryVectorStore.from_documents(docs, embedding=embeddingOllama)

# Use the vectorstore as a retriever
retriever = vectorstore.as_retriever()

# Retrieve the most similar text
retrieved_documents = retriever.get_relevant_documents("sample")
print(retrieved_documents)
