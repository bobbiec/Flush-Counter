from flask import Flask, request
from flask import render_template
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)


app.config.from_object('config')
db = SQLAlchemy(app)
from models import Cluster,Toilet,Flush
migrate = Migrate(app, db)

import test_json as t

@app.route('/')
def home():
    return render_template('index.html',values=jsonify(t))
    # cluster=jsonify(Cluster()), toilet=jsonify(Toilet()),flush=jsonify(Flush())

@app.route('/graphs')
def giraffe():
    return render_template('graphs.html')

@app.route('/map')
def cartography():
    return render_template('map.html')

@app.route('/simulator')
def nogoodnames():
    return render_template('simulator.html')


@app.route('/report-flush', methods=['GET', 'POST'])
def report_flush():
    if request.method == 'GET':
        return "Get not supported on this page"

    # Todo: write to the database
    return "Post success", 200

if __name__ == '__main__':
    app.run()