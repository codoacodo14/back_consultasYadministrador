from flask import Flask, jsonify, request
from models import db, Books, Admins
from flask_bcrypt import Bcrypt
from logging import exception
from flask_cors import CORS
import bcrypt
from flask import jsonify
from flask_jwt_extended import JWTManager, create_access_token
from flask_jwt_extended import jwt_required
import datetime
from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint


bcrypt = Bcrypt()
app = Flask(__name__)
app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'fitomigatito'  
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(minutes=15)
jwt = JWTManager(app)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


with app.app_context():
    db.create_all()

### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Seans-Python-Flask-REST-Boilerplate"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

# Aquí empiezan las rutas
#obtener libros
@app.route("/api/books", methods=["GET"])
def get_books():
    try:
        title = request.args.get("title") or ''
        area = request.args.get("area") or ''
        author = request.args.get("author") or ''
        if title == '' and area == '' and author == '':
            books = Books.query.all()
        else:
            books = Books.query.filter(
                Books.titulo.like(f'%{title}%'),
                Books.autor.like(f'%{author}%'),
                Books.area.like(f'%{area}%')
            ).all()
        books_data = []
        for book in books:
            books_data.append({
                "id": book.id,
                "title": book.title,
                "author": book.author,
                "availability": book.availability,
                "area": book.area
            })
            
        return jsonify(books_data)
        
    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"error": "Ha ocurrido un error"}), 500

#agregar libro  
@app.route("/api/books", methods=["POST"])
@jwt_required()
def add_book():
    
    try:
        data = request.get_json()
        author = data.get('author')
        title = data.get('title')
        editorial = data.get('editorial')
        availability = data.get('availability')
        area = data.get('area')

        if not title or not author or not area or not editorial or not availability:
            return jsonify({"error": "Faltan datos obligatorios"}), 400

        book = Books(author=author, title=title, editorial=editorial, availability=availability, area=area)
        db.session.add(book)
        db.session.commit()
        return jsonify({"message": "Libro agregado exitosamente"})
    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"error": "Ha ocurrido un error"}), 500

#borrar libro
@app.route("/api/books/<int:book_id>", methods=["DELETE"])
@jwt_required()

def delete_book(book_id):
    try:
        # Buscar el libro en la base de datos
        book = Books.query.get(book_id)

        if not book:
            return jsonify({"error": "Libro no encontrado"}), 404

        # Eliminar el libro de la base de datos
        db.session.delete(book)
        db.session.commit()

        return jsonify({"message": "Libro eliminado exitosamente"})
    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"error": "Ha ocurrido un error"}), 500

#actualizar libro    
@app.route("/api/books/<int:book_id>", methods=["PUT"])
@jwt_required()
def update_book(book_id):
    try:
        book = Books.query.get(book_id)

        if not book:
            return jsonify({"error": "Libro no encontrado"}), 404

        data = request.get_json()

        for key, value in data.items():
            setattr(book, key, value)

        db.session.commit()
        return jsonify({"message": "Libro actualizado exitosamente"})
    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"error": "Ha ocurrido un error"}), 500


#Administrador
#registro 
@app.route("/api/register", methods=["POST"])
def register_admin():
    try:
        data = request.get_json()
        name = data.get('name')
        password = data.get('password')

        if not name or not password:
            return jsonify({"error": "Faltan datos obligatorios"}), 400

        admin = Admins.query.filter_by(name=name).first()

        if admin:
            return jsonify({"error": "El administrador ya está registrado"}), 400

        new_admin = Admins(name=name)
        new_admin.set_password(password)
        db.session.add(new_admin)
        db.session.commit()

        return jsonify({"message": "Registro de administrador exitoso"})
    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"error": "Ha ocurrido un error"}), 500

#logueo
@app.route("/api/login", methods=["POST"])
def login_administrador():
    try:
        data = request.get_json()
        name = data.get('name')
        password = data.get('password')

        if not name or not password:
            return jsonify({"error": "Faltan datos obligatorios"}), 400

        admin = Admins.query.filter_by(name=name).first()

        if not admin or not bcrypt.check_password_hash(admin.password_hash, password):
            return jsonify({"error": "Credenciales inválidas"}), 401

        # Generar token de acceso
        token = create_access_token(identity=admin.id)

        return jsonify({"message": "Inicio de sesión exitoso", "token": token})


    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"error": "Ha ocurrido un error"}), 500







if __name__ == "__main__":
    app.run(debug=True, port=4000)

