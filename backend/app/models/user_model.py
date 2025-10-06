from app.database import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    telephone = db.Column(db.String(20), nullable=True)
    role = db.Column(db.String(50), nullable=False, default='user')  # 'admin' o 'user'

    def __init__ (self, first_name, last_name, email, password, role="user"):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.set_password(password)
        self.role = role

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    # Guarda un usuario en la base de datos
    def save(self):
        db.session.add(self)
        db.session.commit()


    # Representación en cadena del objeto User
    #def __repr__(self):
    #    return f"<User {self.email}>"

    @staticmethod
    def fing_by_email(email):
        return User.query.filter_by(email=email).first()