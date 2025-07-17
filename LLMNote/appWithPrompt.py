from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json
import os
import msvcrt

# 🔧 Local LLM setup (LM Studio or compatible)
llm = OpenAI(
    openai_api_base="http://localhost:1234/v1",
    openai_api_key="lm-studio"
)

# 🧾 Known benefit categories for similarity scoring
known_benefits = [
    "Abortion Services",
    "Acupuncture",
    "Preventive Care",
    "Emergency Services",
    "Mental Health",
    "Prescription Drugs",
    "Specialist Visits",
    "Deductible",
    "Coinsurance",
    "Copayment",
    "Out-of-Pocket Maximum"
]

# 🧠 Prompt context
context = """
You are a health insurance benefits analyst.

Your task is to analyze the JSON data below and extract health insurance benefits. 
Focus only on the "Text" field within the "structure" of each note, as this reflects the decision maker’s input.

Instructions:
- Identify and summarize any health insurance benefits mentioned.
- Include notes of both type "Note" and "exclusion".
- If a benefit is referred to, provide a short summary and a cosine similarity score against known benefit categories.
- Only list benefits that are explicitly or implicitly referred to.
"""

# 🧠 Prompt template
prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="{context}\n\nQ: Please analyze the following JSON data:\n{question}\nA:"
)

chain = LLMChain(llm=llm, prompt=prompt)

# 🧮 Cosine similarity function
def get_similarity_score(text, reference_texts):
    vectorizer = TfidfVectorizer().fit_transform([text] + reference_texts)
    vectors = vectorizer.toarray()
    scores = cosine_similarity([vectors[0]], vectors[1:])
    return dict(zip(reference_texts, scores[0]))

# 📤 Extract all "Text" fields from JSON
def extract_texts(json_data):
    notes = json.loads(json_data)
    texts = []

    def recurse(note):
        if "structure" in note:
            for item in note["structure"]:
                if "text" in item:
                    texts.append((note.get("heading", ""), note["type"], item["text"]))
        for sub in note.get("subNotes", []):
            recurse(sub)

    for note in notes if isinstance(notes, list) else [notes]:
        recurse(note)

    return texts

# 📥 Input JSON
question = """
[
    {
        "order": 0,
        "type": "Note",
        "heading": "Maternity and Reproductive Health Services",
        "structure": [],
        "subNotes": [
            {
                "order": 0,
                "type": "Note",
                "heading": "Abortion Services",
                "structure": [
                    {
                        "order": 0,
                        "text": "Benefits for abortions in the case of rape or incest, or for a pregnancy which, as certified by a doctor, places the woman in danger of death unless an abortion is performed (i.e., abortions for which federal funding is allowed)."
                    }
                ],
                "subNotes": []
            }
        ]
    },
    {
        "order": 0,
        "type": "exclusion",
        "heading": "Acupuncture/Nerve Pathway Therapy",
        "structure": [
            {
                "order": 0,
                "text": "Services or supplies related to the use of needles inserted along specific nerve pathways, regardless of the type of Provider performing the service."
            }
        ],
        "subNotes": []
    }
]
"""

# 🧾 Process each note
texts = extract_texts(question)
os.system('cls')
print("Press any key to continue...")
msvcrt.getch()

for heading, note_type, text in texts:
    print(f"\n🔹 Heading: {heading}")
    print(f"📄 Type: {note_type}")
    print(f"📝 Text: {text}")

    # Run LLM summarization
    response = chain.run(context=context, question=text)
    print(f"🧠 Summary: {response.strip()}")

    # Run similarity scoring
    scores = get_similarity_score(text, known_benefits)
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    print("📊 Similarity Scores:")
    for benefit, score in sorted_scores[:3]:  # Top 3 matches
        print(f"   - {benefit}: {score:.2f}")
