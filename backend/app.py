# compose_flask/app.py
from flask import Flask
from redis import Redis

import os
import json

from flask import Flask, Response, request

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def index():
  return '<strong>Index<strong>'

@app.route("/api")
def api():
  users = '{"id": 1, "name": "User-1"}'
  return Response(users, mimetype="application/json", status=200)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)