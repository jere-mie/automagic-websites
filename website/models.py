from website import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(61), nullable=False)
    linkedin = db.Column(db.String(61))
    github = db.Column(db.String(61))
    email = db.Column(db.String(61))
    
    def __repr__(self):
        return f"Username: {self.username}"