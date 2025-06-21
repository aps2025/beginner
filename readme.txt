------ollama-----------
2. get llm model 
3. https://huggingface.co/unsloth/Llama-3.1-8B-Instruct-GGUF
4. Meta-Llama-3-8B-Instruct-bf16-correct-pre-tokenizer-and-EOS-token-Q8_0-Q6_k-Q4_K_M-GGUF
File Modelfile
FROM .

1. -> start server 
	ollama serve
open console
2. create model card specific to Ollama
	c:> ollama create <MODEL_NAME1> <---  will create .ollma binary directly or consider it as file

3. Run/Load the model
	ollama run <MODEL_NAME1> 
4. Client is ready to interact. ask question

5. ollama rm <MODEL_NAME1> 

6. ollama list


----LM Studio-----
install LM studio 
Loaded https://huggingface.co/NikolayKozloff/Meta-Llama-3-8B-Instruct-bf16-correct-pre-tokenizer-and-EOS-token-Q8_0-Q6_k-Q4_K_M-GGUF



