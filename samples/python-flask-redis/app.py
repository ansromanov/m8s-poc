from flask import Flask, request, Response, stream_with_context, jsonify
from redis import Redis
import time
import os
import json

app = Flask(__name__)
db = Redis(host="redis", port=6379)

ttl = 1000


@app.route("/")
def hello():
    db.incr("count")
    return "Count is %s." % db.get("count")


@app.route("/<path:path>", methods=["PUT", "GET"])
def home(path):
    if request.method == "PUT":
        event = request.json
        print(event)
        # event["last_updated"] = time.time()
        # event["ttl"] = ttl
        # db.delete(path)
        # db.hmset(path, event)
        # db.expire(path, ttl)
        # print(jsonify(event))
        return jsonify(event), 201

    if not db.exists(path):
        return "Error: thing does not exist"

    event = db.hgetall(path)
    event["ttl"] = db.ttl(path)
    return jsonify(event), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)