import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

URL = "https://openrouter.ai/api/v1/chat/completions"

HEADERS = {
"Authorization": f"Bearer {OPENROUTER_API_KEY}",
"Content-Type": "application/json"
}

def generate_email_model_a(intent, facts, tone):


    prompt = f"""

Generate a professional email.

Intent:
{intent}

Facts:
{chr(10).join(facts)}

Tone:
{tone}
"""


    response = requests.post(
    url=URL,
    headers=HEADERS,
    data=json.dumps({
        "model": "openai/gpt-oss-120b:free",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.7
    })
)

    result = response.json()

    return result["choices"][0]["message"]["content"]
