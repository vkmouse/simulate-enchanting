from flask import Flask
import json
from simulate_enchanting.repository import MySQLUnitOfWork

app = Flask(__name__)
unitOfWork = MySQLUnitOfWork()
unitOfWork.initialize()

@app.route('/')
def home():
    return 'Hello World!'

@app.route('/attributes')
def serials():
    return json.dumps(unitOfWork.attributeRepository.getAll())

@app.route('/categories')
def serials():
    return json.dumps(unitOfWork.categoryRepository.getAll())

@app.route('/ranges')
def serials():
    return json.dumps(unitOfWork.rangeRepository.getAll())

@app.route('/rows')
def serials():
    return json.dumps(unitOfWork.rowRepository.getAll())

@app.route('/serials')
def serials():
    return json.dumps(unitOfWork.serialRepository.getAll())



if __name__ == "__main__":
    app.run(debug=True)