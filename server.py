from flask import Flask, request, jsonify

app = Flask(__name__)

users = {}  # user_id -> {"lat": float, "lon": float}

@app.route("/update_location", methods=["POST"])
def update_location():
    data = request.json
    user_id = data.get("user_id")
    lat = data.get("lat")
    lon = data.get("lon")
    if not user_id or lat is None or lon is None:
        return jsonify({"error": "Invalid data"}), 400
    users[user_id] = {"lat": lat, "lon": lon}
    return jsonify({"status": "ok"})

@app.route("/get_locations", methods=["GET"])
def get_locations():
    return jsonify(users)

@app.route("/")
def index():
    return "Flask location server is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
