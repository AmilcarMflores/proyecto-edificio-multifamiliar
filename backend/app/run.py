from flask import Flask
from flask_jwt_extended import JWTManager
from controllers.user_controller import user_bp
from flask_swagger_ui import get_swaggerui_blueprint
from database

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "tu_clave_secreta"
SWAGGER_URL = "/api/docs"
API_URL = "/static/swagger.json"

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        "app_name": "Edificio Multifamiliar API"
    }
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

#Configuración de la base de datos postgresql
# mi usuario en postgresql es "amilcar" y mi contraseña es "123456"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://usuario:contraseña@localhost/edificio_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

jwt = JWTManager(app)

app.register_blueprint(user_bp, url_prefix="/api/users")

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
