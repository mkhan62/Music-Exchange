from flask import Flask, render_template
from flask import request

app = Flask(__name__)


stocks = [{"name": "Dive", "artist": "Ed Shereen", "price": 23.5},
          {"name": "Perfect", "artist": "Ed Shereen", "price": 18.5},
          {"name": "Green Light", "artist": "Lorde", "price": 97.1},
          {"name": "Happy", "artist": "Pharrell-Williams", "price": 47.5}]

@app.route('/')
def display_stock():
    return render_template('/index.html', song = stocks[2])

@app.route('/')
def search_stock():
    name = request.args.get('name')
    result = {"name": "NONE", "artist": "NONE", "price": 0.0}
    for stock in stocks:
        if stock["name"] == name:
            result = stock
            break
    return render_template('/index.html', song = result)

@app.route('/hello')
def hello():
    return request.args.get('name')


if __name__ == '__main__':
    app.run()
