from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
# Example documents for retrieval
documents = [
  {"page_content": "LangChain is a framework for developing applications powered by language models."},
  {"page_content": "LangChain provides components for prompt management, chains, and memory."}
  {"page_content": "You can use LangChain with local or cloud-based LLMs."}
]

# Create embeddings and vector store
embeddings = OpenAIEmbeddings(openai_api_base="http://localhost:1234/v1", openai_api_key="lm-studio")
#vectorstore = FAISS.from_documents([doc["page_content"] for doc in documents], embeddings)


vectorstore = FAISS.from_documents([Document(page_content=doc["page_content"]) for doc in documents], embeddings)
#vectorstore = FAISS.from_documents([doc["page_content"] for doc in documents], embeddings)


# Create retriever1`3`
retriever = vectorstore.as_retriever()

# RAG chain: retrieval-augmented generation
rag_chain = RetrievalQA.from_chain_type(
  llm=llm,
  chain_type="stuff",
  retriever=retriever,
  return_source_documents=False
)

# Example RAG usage
rag_response = rag_chain.run({"query": "What is Langchain?"})
print("RAG response:", rag_response)
# Example: Connect to LM Studio's local LLM API (e.g., OpenAI-compatible endpoint)
llm = OpenAI(
    openai_api_base="http://localhost:1234/v1",  # LM Studio's local endpoint
    openai_api_key="lm-studio",  # Dummy key for local endpoints
  #  model_name="TheBloke/Llama-2-7B-Chat-GPTQ"   # Replace with your model name
    #model_name="Meta-Llama-3-8B-Instruct-bf16-correct-pre-tokenizer-and-EOS-token-Q8_0-Q6_k-Q4_K_M-GGUF"
)

prompt = PromptTemplate(
    input_variables=["question"],
    template="Q: {question}\nA:"
)

chain = LLMChain(llm=llm, prompt=prompt)

# Example usage
question = "What is Langchain?"
response = chain.run(question=question)
print(response)
#meta-llama-3-8b-instruct-correct-pre-tokenizer-and-eos-token