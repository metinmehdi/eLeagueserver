from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

ONESIGNAL_APP_ID = "d778e7ef-fd38-4fda-8440-50eacdefc6bc"  # Bura öz APP ID-ni yaz
ONESIGNAL_API_KEY = "ejdo7whqpezpf3egbaw4as6gk"  # Bura öz API KEY-ni yaz

@app.route('/')
def home():
    return "API işləyir boss! 😊"

@app.route('/sendpush', methods=['POST'])
def send_push():
    try:
        # Kodulardan gələn dictionary burda form-data şəklində olacaq
        data = request.form.to_dict(flat=False)

        # Player ID-lər array şəklində gələcək, ona görə [0] lazımdır
        player_ids = data.get("player_ids[]", [])  # Kodular listləri belə göndərir
        if isinstance(player_ids, str):  # Əgər tək string gəlibsə
            player_ids = [player_ids]

        title = data.get("title", [""])[0]
        message = data.get("message", [""])[0]

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

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
