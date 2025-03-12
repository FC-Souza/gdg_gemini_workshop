from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
gemini_key = os.getenv("GEMINI_API_KEY")


# client = genai.Client(api_key="AIzaSyAPfmqfU4Rkd_iLPaKUhWEh4cpa2QJ_emw")
client = genai.Client(api_key=gemini_key)

response = client.models.generate_content_stream(
    model="gemini-2.0-flash",
    contents=["Explain how AI works"])
for chunk in response:
    print(chunk.text, end="")