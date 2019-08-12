import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_pipelines():
    return "Hello, pipelines!"


@app.route("/version")
def version():
    version = os.environ.get("HELLO_PIPELINES_VERSION")
    return f"Version: {version}"
