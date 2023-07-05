from flask import Flask, request
import requests
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

@app.route('/echo', methods=['POST'])
def echo():
    request_body = request.get_json()
    return request_body


@app.route('/proxy')
def proxy():
    r = requests.get('https://pokeapi.co/api/v2/pokemon/eevee',auth=('user','pass'))
    print(r.status_code)
    print(r.headers['content-type'])

    return f'{r.status_code}'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')