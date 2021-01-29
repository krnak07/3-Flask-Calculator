from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)


@app.route('/')
@cross_origin()
def index():
    return render_template('index.html')


@app.route('/eval')
@cross_origin()
def evaluate():
    return str(eval(request.args.get('exp'))), 200


if __name__ == '__main__':
    app.run(debug=True)
