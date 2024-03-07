from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/portal', methods=['GET', 'POST'])
def portal():
    data = request.json
    print(data)
    return jsonify({"mesage": "Data received", "yourData": data}), 200

@app.route('/signup', methods=['POST'])

def signup():
    recieve_data = request.json

if __name__ == '__main__':
    app.run(debug=True)
