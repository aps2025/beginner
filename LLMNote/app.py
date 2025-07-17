from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import os
import msvcrt

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

#text similarty score/ Cosine similarity score
context = (
    #"You are a experience health insurance benefit  representative. "    
    #"Given a string, determine if it refers to a covered benefit under a typical health insurance plan."
    # " Check with structure.text of notes and subnotes and suggest the benefit names for each notes"
    "Based on the JSON data below, please identify and summarize the health insurance benefit. "
    "For this process focus only on the \"Text\" field within the \"structure\" of each note, as this reflects the decision maker’s input."
    "Provide the text similarty score or cosine simliarity score if refered health insurance benefits." 
    "Even for Exclusions type, identify the text and summerize the health insurance benefit."
    "List down only refered benefits."
)
context = ( """
Based on the JSON data below, please identify and summarize the health insurance benefits. 
           Focus exclusively on the "Text" field within the "structure" of each note, as this represents the decision maker’s input. 
           For each note, calculate and provide a text similarity score (e.g., cosine similarity) if the text refers to health insurance benefits. 
           Even for notes with "type": "exclusion", extract and summarize any referenced health insurance benefits. 
           Only list health insurance benefit that are explicitly or implicitly referred to in the text.
 """

)
#"Given the following health insurance policy text in JSON format: 'text': '<<NOTE>>', extract the key health insurance benefits and list them in a structured format (e.g., as a list or JSON array of benefit-value pairs). Consider benefits such as deductible, coinsurance, copayment, allowed amount, out-of-pocket maximum, covered services (e.g., preventive care, specialist visits, prescription drugs, mental health, emergency care), and eligibility criteria."
#"Given a string, determine if it refers to a covered benefit under a typical health insurance plan."
#Given the following health insurance policy text in JSON format: {'text': '<<POLICY TEXT HERE>>'}, extract the key health insurance benefits and list them in a structured format (e.g., as a list or JSON array of benefit-value pairs). Consider benefits such as deductible, coinsurance, copayment, allowed amount, out-of-pocket maximum, covered services (e.g., preventive care, specialist visits, prescription drugs, mental health, emergency care), and eligibility criteria."


chain = LLMChain(llm=llm, prompt=prompt)

# Example usage
#question = "What is Langchain?"
bnft = "Abortion"
prompt.template = (
    context + "\n"
    #"Q: Does the following string refer to a benefit? \"{question}\"\nA:"
    "Q: Please analyze the following JSON data to identify and summarize health insurance benefits. \"{question}\"\nA:"
)
question = """
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
                                "type": "Note",
                                "heading": "Acupuncture/Nerve Pathway Therapy",
                                "structure": [
                                    {
                                        "order": 0,
                                        "text": "Services or supplies related to the use of needles inserted along specific nerve pathways, regardless of the type of Provider performing the service."
                                    }
                                ],
                                "subNotes": []
                            }

"""
response = chain.run(question=question)
os.system('cls')
print("Press any key to continue...")
msvcrt.getch()
print(response)
#meta-llama-3-8b-instruct-correct-pre-tokenizer-and-eos-token
