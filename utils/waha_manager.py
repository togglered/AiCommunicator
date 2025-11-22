import requests
import os


class WahaManager:
    API_URL = os.getenv("WAHA_API_URL", "http://localhost:3000/api")

    @classmethod
    def send_message(cls, reciever: str, message: str) -> None:
        url = cls.API_URL + "/sendMessage"
        data = {
            "session": "default",
            "chatId": reciever,
            "text": message
        }
        response = requests.post(url, json=data)
        return response.status
