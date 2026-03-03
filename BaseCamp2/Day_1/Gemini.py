# Import required class from Google
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

# Initialise an client object with API key
load_dotenv ()
client = genai.Client()

Client = genai.Client (api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(
                model="gemini-2.5-flash", 
                contents="I am not a hardware specialist. Explain GPU vs TPU to me."
            )
print(response.text)

# There is a specific instruction given 
Instruction = "Continue the statement and make it 50 words"
Statement  = "When we get to see new AI models every week ..."
# Statement  = "Though we get to see new AI models every week ..."
# Statement  = "RAG is useful in scenarios ..."

# Invoke multiple times ...
# ?? What do we expect 
for i in range (3):
    
    response = client.models.generate_content(
                    model="gemini-2.5-flash-lite",
                    # model="gemini-flash-lite-latest",
                    config =types.GenerateContentConfig(
                                system_instruction=Instruction,),
                    contents =Statement
    )

    print(response.text)