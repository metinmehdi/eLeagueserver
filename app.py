from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sendpush', methods=['POST'])
def send_push():
    data = request.form.to_dict(flat=False)
    print("Tam data:", data)
    return jsonify({"data": data})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
