from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

@app.route('/', methods=['POST'])
def anything():
    request_body = request.get_json()

    return request_body

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')