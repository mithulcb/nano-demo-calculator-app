import flask as fl

app = fl.Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'

@app.route("/calculator/add", methods=['POST'])
def add():
    get_number = fl.request.json
    response = int(get_number['first'] + get_number['second'])
    return fl.jsonify(response)

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    get_number = fl.request.json
    response = int(get_number['first'] - get_number['second'])
    return fl.jsonify(response)

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
