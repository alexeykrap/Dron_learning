from flask import Flask, request, jsonify
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

drone_state = {
    "status": "landed",
    "position": {
        "latitude":  0.0,
        "longitude": 0.0,
        "altitude":  0.0,
    }
}


@app.route("/drone/takeoff", methods=["POST"])
def takeoff():
    try:
        if drone_state["status"] == "flying":
            return jsonify({
                "error": "Дрон уже в воздухе!"
            }), 400
        drone_state["status"] = "flying"
        drone_state["position"]["altitude"] = 10.0

        app.logger.info("Дрон взлетел")
        return jsonify({
            "message": "Взлёт выполнен",
            "drone_state": drone_state,
        }), 200
    except Exception as e:
        app.logger.error(f"Ошибка при взлёте: {str(e)}")
        return jsonify({
            "error": "Ошибка при взлёте"
        }), 500


if __name__ == "__main__":
    app.run(debug=True)