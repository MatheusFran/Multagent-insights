from flask import Flask

from src.supervisor import create_supervisor
import requests
import json

app = Flask(__name__)
supervisor = create_supervisor()


@app.route("/ask", methods=["POST"])
def ask():
    data = requests.get_json()
    user_input = data.get("query", "")

    if not user_input:
        return json.load({"error": "Campo 'query' é obrigatório"}), 400

    try:
        result = supervisor.invoke({"messages": [("user", user_input)]})
        return jsonify({"response": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)