from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

ONESIGNAL_APP_ID = "d778e7ef-fd38-4fda-8440-50eacdefc6bc"
ONESIGNAL_API_KEY = "ejdo7whqpezpf3egbaw4as6gk
	"

@app.route('/sendpush', methods=['POST'])
def send_push():
    data = request.get_json()
    player_ids = data.get("player_ids")
    title = data.get("title", "Bildiriş")
    message = data.get("message", "Yeni məlumat")

    payload = {
        "app_id": ONESIGNAL_APP_ID,
        "include_player_ids": player_ids,
        "headings": {"en": title},
        "contents": {"en": message}
    }

    response = requests.post(
        "https://onesignal.com/api/v1/notifications",
        headers={
            "Authorization": f"Basic {ONESIGNAL_API_KEY}",
            "Content-Type": "application/json"
        },
        json=payload
    )

    return jsonify({"status": "ok", "response": response.json()})


if __name__ == '__main__':
    app.run()
