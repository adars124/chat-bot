from langchain.llms import AI21
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('AI21_API_KEY')

os.environ['AI21_API_KEY'] = api_key

def generate_text(text: str) -> str:
    llm = AI21(maxTokens=1000, temperature=0.9, numResults=1)
    
    data = llm(text)

    return data