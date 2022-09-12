from flask import Flask
from flask_cors import CORS

app=Flask(__name__)
CORS(app, resources={r"/.*": {"origins": ["http://localhost/*","https://vkmouse.github.io/*"]}})

@app.route('/')
def hello_world():
    return 'Hello from Flask!'
