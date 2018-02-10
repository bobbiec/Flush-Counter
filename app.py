from flask import Flask, request
from flask import render_template


app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
def home():
    return render_template('index.html')

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