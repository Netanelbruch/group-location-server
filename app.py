from flask import Flask, request, jsonify
from flask_cors import CORS
import time, uuid

app = Flask(__name__)
CORS(app)

# מילון שיחזיק את כל הקבוצות
groups = {}

@app.route("/")
def home():
    return "✅ Flask group location server is running on Render!"

@app.route("/create_group", methods=["POST"])
def create_group():
    group_id = str(uuid.uuid4())[:8]  # מזהה קצר לקבוצה
    groups[group_id] = {}
    return jsonify({"group_id": group_id}), 200

@app.route("/update_location/<group_id>", methods=["POST"])
def update_location(group_id):
    if group_id not in groups:
        return jsonify({"status": "error", "message": "group not found"}), 404

    data = request.get_json()
    user = data.get("user")
    lat = data.get("lat")
    lon = data.get("lon")

    if user and lat and lon:
        groups[group_id][user] = {
            "lat": lat,
            "lon": lon,
            "last_update": time.time()
        }
        return jsonify({"status": "success"}), 200

    return jsonify({"status": "error", "message": "missing data"}), 400

@app.route("/get_locations/<group_id>", methods=["GET"])
def get_locations(group_id):
    if group_id not in groups:
        return jsonify({"status": "error", "message": "group not found"}), 404

    return jsonify(groups[group_id]), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
