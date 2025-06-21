from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.embeddings import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(openai_api_key="your-openai-api-key")
vector = embeddings.embed_query("Hello world")
print(vector)
# testLangChainRag.py


# Sample documents
docs = [
    "The Eiffel Tower is located in Paris.",
    "The Great Wall of China is visible from space.",
    "Python is a popular programming language."
]

# Split documents into chunks
text_splitter = CharacterTextSplitter(chunk_size=50, chunk_overlap=0)
documents = []
for doc in docs:
    documents.extend(text_splitter.split_text(doc))

# Create embeddings and vector store
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_texts(documents, embeddings)

# Set up retriever
retriever = vectorstore.as_retriever()

# Set up LLM
llm = OpenAI(temperature=0)

# Create RetrievalQA chain
qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever
)

# Ask a question
query = "Where is the Eiffel Tower?"
result = qa.run(query)
print("Q:", query)
print("A:", result)