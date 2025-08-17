from flask import Flask, request, jsonify
from flask_cors import CORS
import time

server = Flask(__name__)
CORS(server)

# נשמור את כל המיקומים של המשתמשים בזיכרון
locations = {}

@server.route("/")
def home():
    return "✅ Flask location server is running on Render!"

@server.route("/update_location", methods=["POST"])
def update_location():
    data = request.get_json()
    user = data.get("user")
    lat = data.get("lat")
    lon = data.get("lon")
    if user and lat and lon:
        locations[user] = {
            "lat": lat,
            "lon": lon,
            "last_update": time.time()
        }
        return jsonify({"status": "success"}), 200
    return jsonify({"status": "error", "message": "missing data"}), 400

@server.route("/get_locations", methods=["GET"])
def get_locations():
    return jsonify(locations)

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=10000)
