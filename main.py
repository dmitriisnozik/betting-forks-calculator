from flask import Flask, render_template, request
from calc import Calculation


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index(result=None):
    if request.method == 'POST' and all(
            [request.form['amount'], request.form['odd1'], request.form['odd2']]
    ):
        rounding = -1 if request.form.get('rounding') else 2
        result = Calculation.calculation(
            float(request.form['amount']),
            float(request.form['odd1']),
            float(request.form['odd2']),
            rounding=rounding,
        )
    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
