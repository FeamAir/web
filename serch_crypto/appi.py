from flask import Flask, render_template

from utils import crypto
from webargs.flaskparser import use_kwargs
from webargs import fields
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/rates")
@use_kwargs(
    {
        'currency': fields.Str(required=True)
    },
    location='query'
)
def serch_crypto(currency):
    result = crypto(currency)
    return render_template('serch_currency.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
