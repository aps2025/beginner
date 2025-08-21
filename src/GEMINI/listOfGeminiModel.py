import google.generativeai as genai
import os

# Configure the API key
genai.configure(api_key="AIzaSyCqIlp7mTSarIsucoFy7snPp1uweso6T5w")
print("API key configured."         )
# Get and print the list of available models
models = list(genai.list_models())
print(f"Number of models: {len(models)}")
unique_methods = set()
for m in models:
    unique_methods.update(m.supported_generation_methods)
print("Unique supported_generation_methods:")
for method in unique_methods:
    print(method)

for m in genai.list_models():
    print(f"{m.supported_generation_methods}::{m.name}")
    # Only print models that support text generation
    #if 'generateContent' in m.supported_generation_methods:
    #    print(m.name)