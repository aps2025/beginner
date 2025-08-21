import google.generativeai as genai
from PIL import Image
import io

# 🔐 Set your API key
genai.configure(api_key="AIzaSyCqIlp7mTSarIsucoFy7snPp1uweso6T5w")

# 🧠 Load Gemini 2.5 Pro (multimodal)
model = genai.GenerativeModel("gemini-2.5-pro")

# 📷 Load your image
image_path = "C:\\Users\\AL12918\\src\\beginner\\src\\GEMINI\\multiModal\\your_image.jpg"
print(f"Image path:{image_path}")

with open(image_path, "rb") as f:
    image_data = f.read()

# 🧾 Run OCR-like prompt
response = model.generate_content(
    [
        "Extract all readable text from this image. Return only the text content.",
        {"mime_type": "image/png", "data": image_data}
    ]
)

# 🖨️ Print the result
print(response.text)
