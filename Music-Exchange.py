from flask import Flask, render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_world():
    mytodos = ["Hi, this is a todo", "Hi, this is a todo", "Hi, this is a todo", "Hi, this is a todo"]
    return render_template('/index.html', todos = mytodos)

@app.route('/hello')
def hello():
    return request.args.get('name')


if __name__ == '__main__':
    app.run()
