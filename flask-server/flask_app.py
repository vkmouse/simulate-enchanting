from flask import Flask
from flask_cors import CORS
from enchantment_database import createMySQLEnchantmentDatabase

app = Flask(__name__)
CORS(app, resources={r"/.*": {"origins": ["http://localhost/*","https://vkmouse.github.io/*"]}})
db = createMySQLEnchantmentDatabase()

@app.route('/')
def hello_world():
    return '2022/09/12'
