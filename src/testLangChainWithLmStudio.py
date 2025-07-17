from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

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