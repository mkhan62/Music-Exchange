from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/hello')
def hello():
    return request.args.get('name')


if __name__ == '__main__':
    app.run()
