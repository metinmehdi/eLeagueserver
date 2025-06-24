@app.route('/sendpush', methods=['POST'])
def send_push():
    try:
        data = request.get_json()
        print("Gelen JSON:", data)

        player_ids = data.get("player_ids", [])
        title = data.get("title", "")
        message = data.get("message", "")

        print("player_ids:", player_ids)
        print("title:", title)
        print("message:", message)

        if not player_ids or not title or not message:
            return jsonify({"status": "error", "message": "Eksik bilgi"}), 400

        return jsonify({"status": "ok", "player_ids": player_ids, "title": title, "message": message})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
