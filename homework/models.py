from homework import app, db

# Import for Werkzeug Security
from werkzeug.security import generate_password_hash, check_password_hash

# Import for Date Time Module
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(150), nullable = False, unique = True)
    email = db.Column(db.String(150), nullable = False, unique = True)
    password = db.Column(db.String(256), nullable = False)
    post = db.relationship('Post', backref = 'author', lazy = True )

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = self.set_password(password)

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def __repr__(self):
            return f'{self.username} has been created with {self.email}'


class Phone(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(200))
    last_name = db.Column(db.String(300))
    area_code = db.Column(db.Integer)
    number = db.Column(db.String(300))
    date_create = db.Column(db.DateTime, nullable = False, default = datetime.utctimetuple )
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    def __init__(self,first_name, last_name, area_code, number, user_id):
        self.first_name = first_name
        self.last_name - last_name
        self.area_code = area_code
        self.number = number
        self.user_id = user_id

    def __repr__(self):
        return f'Thank you, {self.first_name} for signing up!.'