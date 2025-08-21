from langchain_community.llms import Ollama

# Initialize the Ollama LLM with your desired model (e.g., 'llama2')
llm = Ollama(model="llama2")

# Example prompt
prompt = "What is the capital of France?"

# Get response from the LLM
response = llm(prompt)

print("Response:", response)