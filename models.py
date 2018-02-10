from app import db

class Cluster(db.Model):
    __tablename__ = 'clusters'

    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.Integer) # 0 for unisex, 1 men's, 2 women's
    num_toilets = db.Column(db.Integer)
    location = db.Column(db.String(21)) # Format +12.345678,-98.765432 (lat, long)
    building_num = db.Column(db.Integer)
    floor_num = db.Column(db.Integer)
    toilets = db.relationship('Toilet', backref='cluster', lazy=True)

    def __repr__(self):
        return "Building %s, Floor %s" % (self.building_num, self.floor_num)

class Toilet(db.Model):
    __tablename__ = 'toilets'

    id = db.Column(db.Integer, primary_key=True)
    flushes = db.relationship('Flush', backref='toilet', lazy=True)
    flush_volume = db.Column(db.Integer) # In gallons
    big_small = db.Column(db.Boolean) # Whether this can handle big/small flushes or not
    
    cluster_id = db.Column(db.Integer, db.ForeignKey('cluster.id'))
    cluster_pos = db.Column(db.Integer)

    def __repr__(self):
        return "Toilet(%s, Toilet %s)" % (self.cluster, self.cluster_pos)

class Flush(db.Model):
    __tablename__ = 'flushes'

    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime, nullable=False)
    toilet_id = db.Column(db.Integer, db.ForeignKey('toilet.id'))
    flush_type = db.Column(db.Integer) # 0 for big, 1 for small

    def __repr__(self):
        return "Flush(%s from toilet=%s)" % (self.time, self.toilet)