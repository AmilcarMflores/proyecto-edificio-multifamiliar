import json
from database import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# Tenemos dos tipos de usuarios: admin y residente
class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(50), nullable=False)  # 'admin' o 'user'

    def __init__ (self, first_name, last_name, email, password, role="user"):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.set_password(password)
        # Almacena el rol como un JSON string
        self.role = json.dumps(role)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # Guarda un usario en la base de datos
    def save(self):
        db.session.add(self)
        db.session.commit()
