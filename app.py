from flask import Flask
import socket
import datetime
import os

app = Flask(__name__)

@app.route("/")
def home():
    return f"""
    <h1>VERSION NUEVA 🔥</h1>
    <p>Hostname: {socket.gethostname()}</p>
    <p>Fecha: {datetime.datetime.now()}</p>
    """
@app.route("/env")
def env():
    return f"ENV: {os.getenv('ENVIRONMENT', 'dev')}"

app.run(host="0.0.0.0", port=5000)
