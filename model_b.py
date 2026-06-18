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

def generate_email_model_b(intent, facts, tone):


    prompt = f"""

You are a senior executive communications specialist.

Your task is to write professional business emails.

Rules:

1. Include EVERY fact.
2. Match the requested tone.
3. Write naturally.
4. Include:

   * Subject
   * Greeting
   * Body
   * Closing

Example:

Intent: Thank Customer

Facts:

* Purchased premium package
* Support available 24/7

Tone: Warm

Output:

Subject: Thank You For Your Purchase

Dear Customer,

Thank you for choosing our premium package.
Our support team is available 24/7 should you need assistance.

Best regards,
Support Team

Generate the email.

Intent:
{intent}

Facts:
{chr(10).join('- ' + x for x in facts)}

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
        "temperature": 0.4
    })
)

    result = response.json()

    return result["choices"][0]["message"]["content"]

