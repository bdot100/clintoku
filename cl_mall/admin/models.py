from cl_mall import db
from cl_mall import app

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), unique=False, nullable=False)
    username = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(180), unique=False, nullable=False)
    is_admin = db.Column(db.Boolean, default=True, nullable=False)
    profile = db.Column(db.String(80), unique=False, nullable=False, 
                        default='profile.jpg')
    
    def __repr__(self):
        return '<User %r>' % self.username
    

with app.app_context():
    db.create_all()
