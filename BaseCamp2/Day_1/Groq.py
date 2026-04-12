from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize Groq client securely
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Your prompt
prompt = "ML vs GenAI?"

# Create message structure
messages = [
    {
        "role": "user",
        "content": prompt
    }
]

try:
    # Create chat completion
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        temperature=0.7,
        max_tokens=500
    )

    # Print response
    print(completion.choices[0].message.content)

except Exception as e:
    print("Error:", e)