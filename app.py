from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)


app.config.from_object('config')
db = SQLAlchemy(app)
from models import Cluster,Toilet,Flush
migrate = Migrate(app, db)

@app.route('/')
def home():
    return render_template('index.html',values)

@app.route('/graphs')
def giraffe():
    return render_template('graphs.html')

@app.route('/map')
def cartography():
    return render_template('map.html')

@app.route('/simulator')
def nogoodnames():
    return render_template('simulator.html')

@app.route('/report-flush', methods=['POST'])
def report_flush():
    data = request.get_json()
    flush = data_to_flush(data)
    if not flush:
        return 'Invalid data', 400
    db.session.add(flush)
    db.session.commit()
    return 'Success', 200

def data_to_flush(data):
    f = Flush()
    f.time = data.get(time)
    f.toilet_id = data.get(toilet_id)
    f.flush_type = data.get(flush_type)
    if f.time is None or f.toilet_id is None or f.flush_type is None:
        return False
    return f

@app.route('/get-all')
def get_all():
    f = Flush.query.all()
    flushes = [a.serialize() for a in f]
    return jsonify(flushes)


def seed_data():
    return None 
    # Initially used to seed data
    """
    # Clusters
    cuc2m = Cluster()
    cuc2m.id = 1
    cuc2m.gender = 2
    cuc2m.location = '+12.345678,-98.765432'
    cuc2m.building_num = 1
    cuc2m.floor_num = 2
    db.session.add(cuc2m)
    db.session.commit()

    cuc2f = cuc2m 
    cuc2f.id = 2
    cuc2f.gender = 3
    db.session.add(cuc2f)
    db.session.commit()

    Toilets

    for i in range(1, 5):
        t = Toilet()
        t.flush_volume = 2
        t.big_small = False
        t.id = i
        t.cluster_id = 1
        t.cluster_pos = i
        db.session.add(t)
    db.session.commit()

    for i in range(1, 7):
        t = Toilet()
        t.flush_volume = 2
        t.big_small = False
        t.id = i + 4
        t.cluster_id = 2
        t.cluster_pos = i
        db.session.add(t)
    db.session.commit()

    Flushes
    import random
    import datetime

    t = datetime.datetime(2018, 2, 9, 8, 0, 0)
    men_ids = list(range(1, 5))
    for id in [random.choice(men_ids) for i in range(30)]:
        t = t + datetime.timedelta(minutes=random.randrange(13))
        f = Flush()
        f.time = t
        f.toilet_id = id
        f.flush_type = 0
        db.session.add(f)
    db.session.commit()
    
    t = datetime.datetime(2018, 2, 9, 8, 0, 0)
    women_ids = list(range(5, 11))
    for id in [random.choice(women_ids) for i in range(100)]:
        t = t + datetime.timedelta(minutes=random.randrange(4))
        f = Flush()
        f.time = t
        f.toilet_id = id
        f.flush_type = 0
        db.session.add(f)

    db.session.commit()
    """

if __name__ == '__main__':
    app.run()