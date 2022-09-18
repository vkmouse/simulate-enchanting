import flask
import flask_cors
import json
from simulate_enchanting.parser import Parser
from simulate_enchanting.repository import MySQLWorker, MySQLUnitOfWork, MemoryUnitOfWork

unitOfWork = None
if MySQLWorker.isAvailable():
    unitOfWork = MySQLUnitOfWork()
else:
    unitOfWork = MemoryUnitOfWork()
unitOfWork.initialize()

app = flask.Flask(__name__)
flask_cors.CORS(app, resources={r"/.*": {"origins": ["http://localhost/*", "https://vkmouse.github.io/*"]}})

@app.route('/')
def home():
    return 'Hello World!'

@app.route('/attributes')
def attributes():
    if 'serial_id' in flask.request.args:
        serialId = int(flask.request.values.get('serial_id'))
        return json.dumps(unitOfWork.attributeRepository.getBySerialId(serialId), ensure_ascii=False)
    return json.dumps(unitOfWork.attributeRepository.getAll(), ensure_ascii=False)

@app.route('/categories')
def categories():
    return json.dumps(unitOfWork.categoryRepository.getAll(), ensure_ascii=False)

@app.route('/ranges')
def ranges():
    return json.dumps(unitOfWork.rangeRepository.getAll(), ensure_ascii=False)

@app.route('/rows')
def rows():
    return json.dumps(unitOfWork.rowRepository.getAll(), ensure_ascii=False)

@app.route('/serials')
def serials():
    return json.dumps(unitOfWork.serialRepository.getAll(), ensure_ascii=False)

@app.route("/notices", methods=['POST'])
def notices():
    notice = flask.request.form.get('notice')
    notice = json.loads(notice)
    parser = Parser()
    result = parser.parse(notice)
    unitOfWork.serialRepository.add(result['Serial'])
    for i in result['Categories']: unitOfWork.categoryRepository.add(i)
    for i in result['Ranges']: unitOfWork.rangeRepository.add(i)
    for i in result['Rows']: unitOfWork.rowRepository.add(i)
    for i in result['Attributes']: unitOfWork.attributeRepository.add(i)
    return ''

if __name__ == "__main__":
    app.run()