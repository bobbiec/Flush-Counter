from app import db

###
# Quick guide to magic numbers
###
# Gender:
# 1. Unisex
# 2. Male
# 3. Female 
#
# Building Number:
# 1. CUC
# 2. Wean Hall
#
# Flush type:
# 1. Normal
# 2. Reduced

class Cluster(db.Model):
    __tablename__ = 'clusters'

    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.Integer) # 1 for unisex, 2 men's, 3 women's
    location = db.Column(db.String(21)) # Format +12.345678,-98.765432 (lat, long)
    building_num = db.Column(db.Integer)
    floor_num = db.Column(db.Integer)
    toilets = db.relationship('Toilet', backref='cluster', lazy=True)

    def serialize(self):
        return {'id':self.id,
                'gender':self.gender,
                'location':self.location,
                'building_num':self.building_num,
                'floor_num':self.floor_num}

    def __repr__(self):
        return 'Building %s, Floor %s' % (self.building_num, self.floor_num)

class Toilet(db.Model):
    __tablename__ = 'toilets'

    id = db.Column(db.Integer, primary_key=True)
    flushes = db.relationship('Flush', backref='toilet', lazy=True)
    flush_volume = db.Column(db.Integer) # In gallons
    big_small = db.Column(db.Boolean) # Whether this can handle big/small flushes or not
    
    cluster_id = db.Column(db.Integer, db.ForeignKey('clusters.id'))
    cluster_pos = db.Column(db.Integer)

    def serialize(self):
        return {'id':self.id,
                'flush_volume':self.flush_volume,
                'big_small':self.big_small,
                'cluster_pos':self.cluster_pos}

    def __repr__(self):
        return 'Toilet(%s, Toilet %s)' % (self.cluster, self.cluster_pos)

class Flush(db.Model):
    __tablename__ = 'flushes'

    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime, nullable=False)
    toilet_id = db.Column(db.Integer, db.ForeignKey('toilets.id'))
    flush_type = db.Column(db.Integer) # 0 for big, 1 for small

    def serialize(self):
        return {'id':self.id,
                'time':self.time.isoformat(),
                'toilet_id':self.toilet_id,
                'flush_type':self.flush_type,
                'toilet':self.toilet.serialize(),
                'cluster':self.toilet.cluster.serialize()}

    def __repr__(self):
        return 'Flush(%s from toilet=%s)' % (self.time, self.toilet)