from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

ONESIGNAL_APP_ID = "d778e7ef-fd38-4fda-8440-50eacdefc6bc"
ONESIGNAL_API_KEY = "ejdo7whqpezpf3egbaw4as6gk"

@app.route('/')
def home():
    return "API işləyir boss! 😊"

@app.route('/sendpush', methods=['POST'])
def send_push():
    data = request.get_json()

    player_ids = data.get("player_ids", [])
    title = data.get("title", "")
    message = data.get("message", "")

    if not player_ids or not title or not message:
        return jsonify({"status": "error", "message": "Eksik bilgi"}), 400

    payload = {
        "app_id": ONESIGNAL_APP_ID,
        "include_player_ids": player_ids,
        "headings": {"en": title},
        "contents": {"en": message}
    }

    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": f"Basic {ONESIGNAL_API_KEY}"
    }

    response = requests.post("https://onesignal.com/api/v1/notifications", json=payload, headers=headers)

    return jsonify({"status": "ok", "response": response.json()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
