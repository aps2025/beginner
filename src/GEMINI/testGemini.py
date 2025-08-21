#AIzaSyD1LUZ7WO0stQQrWcA6wS3cr1KETJtogPc
#AIzaSyCqIlp7mTSarIsucoFy7snPp1uweso6T5w

import google.generativeai as genai
import os

# Configure the API key. It's best practice to use an environment variable.
genai.configure(api_key="AIzaSyCqIlp7mTSarIsucoFy7snPp1uweso6T5w")
print("API key configured.")
# Create a GenerativeModel instance. The 'gemini-pro' model is great for text-only prompts.
model = genai.GenerativeModel('gemini-2.5-pro-preview-03-25')
print("Model instance created: " + str(model))
# Send a prompt to the model and get a response.
response = model.generate_content("What is the capital of France?")

# Print the model's response.
print(response.text)