import torch
from transformers import AutoTokenizer, AutoModel

# Load BioBERT model and tokenizer
model_name = "dmis-lab/biobert-base-cased-v1.1"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# Example biomedical sentence
sentence = "Aspirin is used to reduce fever and relieve mild to moderate pain."

# Tokenize input
inputs = tokenizer(sentence, return_tensors="pt")

# Get model outputs
with torch.no_grad():
    outputs = model(**inputs)

# Get the last hidden state
last_hidden_state = outputs.last_hidden_state

print("Tokenized input:", tokenizer.convert_ids_to_tokens(inputs['input_ids'][0]))
print("Last hidden state shape:", last_hidden_state.shape)