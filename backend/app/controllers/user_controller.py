from flask import Blueprint, request, jsonify
from models.user_model import User
from flask_jwt_extended import create_access_token
from werkezug.security import check_password_hash

user_bp = Blueprint('user', __name__)

@user_bp.route('/register' , methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Se require correo y contraseña"}), 400
    
    existing_user = User.fing_by_email(email)
    if existing_user:
        return jsonify({"error": "El correo ya está registrado"}), 400
    
    new_user = User(email, password)
    new_user.save()

    return jsonify({"message": "Usuario registrado exitosamente"}), 201

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    user = User.fing_by_email(email)
    if user and check_password_hash(user.password_hash, password):
        access_token = create_access_token(identity=email)
        return jsonify({"access_token": access_token}), 200
    else:
        return jsonify({"error": "Credenciales inválidas"}), 401