from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

import asyncio
import os


class AiManager:
    MODEL = os.getenv("AI_MODEL", "gpt-4")
    CLIENT = OpenAI(
        base_url=os.getenv("AI_BASE_URL"),
        api_key=os.getenv("OPENAI_API_KEY"),
        max_retries=3
    )

    @classmethod
    async def convert_messages(cls):
        pass

    @classmethod
    def ask_ai(cls, promt: str, messages_history: list = []) -> str:
        response = cls.CLIENT.chat.completions.create(
            model=cls.MODEL,
            messages=[
                {
                    "role": "system",
                    "content": os.getenv("SYSTEM_PROMT", "You are a helpful assistant.")
                },
                {
                    "role": "user", 
                    "content": promt
                },
                *messages_history
            ]
        )
        return response.choices[0].message.content