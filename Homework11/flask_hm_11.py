from flask import Flask, render_template
from utils import connection, best_selling

app = Flask(__name__)


@app.route('/')
def start():
    return render_template('index.html')


@app.route('/best_selling/<int:sale>')
def best_seller(sale):
    connection()
    b_sell = best_selling(sale)
    return render_template('tracks/best_seller.html', tracks=b_sell)


if __name__ == '__main__':
    app.run(debug=True, port=5050)
