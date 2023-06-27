from flask import Flask, jsonify, request, render_template, redirect, url_for
from models import db, Libros
from logging import exception

app = Flask(__name__, static_url_path="/static")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

with app.app_context():
    db.create_all()

# Aquí empiezan las rutas


@app.route("/")
def home():
    return render_template("nosotros/nosotros.html")


@app.route("/events")
def events():
    return render_template("events/events.html")


@app.route("/library")
def library():
    return render_template("library/library.html")


@app.route("/consultas")
def busqueda():
    titulo = request.args.get("titulo") or ''
    area = request.args.get("area") or ''
    autor = request.args.get("autor") or ''
    try:
        if titulo == '' and area == '' and autor == '':
            libros = Libros.query.all()
        else:
            libros = Libros.query.filter(
                Libros.titulo.like(f'%{titulo}%'),
                Libros.autor.like(f'%{autor}%'),
                Libros.area.like(f'%{area}%')
            ).all()
    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify("Ha ocurrido un error"), 500
    return render_template("consultas/consultas.html",
                           libros=libros,
                           titulo=titulo,
                           autor=autor,
                           area=area
                           )


@app.route("/administrador", methods=['GET', 'POST'])
def administrador():
    if request.method == 'GET':
        return render_template("administrador/administrador.html")
    libro = Libros(**request.form)
    db.session.add(libro)
    db.session.commit()
    return redirect(url_for('busqueda'))


@app.route("/contact")
def contact():
    return render_template("contact/contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=4000)
