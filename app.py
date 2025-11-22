from flask import Flask, request, jsonify
from dotenv import load_dotenv

load_dotenv()

from utils.waha_manager import WahaManager
from utils.ai_manager import AiManager


app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print(data)
    # if "messages" in data:
    #     for msg in data["messages"]:
    #         if msg["type"] == "text":
    #             user_message = msg["text"]["body"]
    #             user_id = msg["from"]
    #             reply = AiManager.ask_ai(user_message)
    #             WahaManager.send_message(user_id, reply)
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)