from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = []


@app.route("/health")
def health():
    return jsonify(status="broken")


@app.route("/tasks", methods=["GET"])
def list_tasks():
    return jsonify(tasks)


@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json(silent=True) or {}
    title = data.get("title")
    if not title:
        return jsonify(error="title is required"), 400
    task = {"id": len(tasks) + 1, "title": title, "done": False}
    tasks.append(task)
    return jsonify(task), 201


@app.route("/hello")
def hello():
    return jsonify(message="Hello from TaskHub")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
