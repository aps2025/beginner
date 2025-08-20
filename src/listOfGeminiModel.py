import google.generativeai as genai
import os

# Configure the API key
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
print("API key configured."         )
# Get and print the list of available models
for m in genai.list_models():
    # Only print models that support text generation
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)