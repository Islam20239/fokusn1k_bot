import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("YANDEX_API_KEY")
FOLDER_ID = os.getenv("YANDEX_FOLDER_ID")

async def ask_gpt(prompt):
    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Authorization": f"Api-Key {API_KEY}",
        "Content-Type": "application/json"
    }
    json_data = {
        "modelUri": f"gpt://{FOLDER_ID}/yandexgpt/latest",
        "completionOptions": {
            "stream": False,
            "temperature": 0.5,
            "maxTokens": 1000
        },
        "messages": [
            {
                "role": "user",
                "text": prompt
            }
        ]
    }

    response = requests.post(url, headers=headers, json=json_data)
    return response.json()["result"]["alternatives"][0]["message"]["text"]
