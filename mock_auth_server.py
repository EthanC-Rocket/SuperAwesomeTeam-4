
from flask import Flask, jsonify, request

app = Flask(__name__)

VALID_TOKEN = "mysecrettoken"

@app.route('/auth', methods=['POST', 'GET'])
def authenticate():
    # Try to get token from header first, then from JSON body
    token = request.headers.get('Authorization')
    if not token:
        if request.is_json:
            token = request.json.get('token')
    # Check token
    if token != VALID_TOKEN:
        return jsonify({"error": "Invalid or missing token."}), 401
    return jsonify({
        "name": "Jane Doe",
        "title": "AI Developer"
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)
