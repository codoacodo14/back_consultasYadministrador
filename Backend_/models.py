from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Libros(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    autor = db.Column(db.String(200), nullable=False)
    titulo = db.Column(db.String(200), nullable=False)
    editorial = db.Column(db.String(100), nullable=False)
    fecha_edicion = db.Column(db.Integer)
    lugar_edicion = db.Column(db.String(100))
    area = db.Column(db.String(50), nullable=False)

    def __init__(self, autor, titulo, editorial, fecha_edicion, lugar_edicion, area):
        super().__init__()
        self.autor = autor
        self.titulo = titulo
        self.editorial = editorial
        self.fecha_edicion = fecha_edicion
        self.lugar_edicion = lugar_edicion
        self.area = area

    def __str__(self):
        return "\nAutor: {}. Titulo: {}. Editorial: {}. Fecha de Edición: {}. Lugar de Edición: {}. Área: {}\n".format(
            self.autor,
            self.titulo,
            self.editorial,
            self.fecha_edicion,
            self.lugar_edicion,
            self.area
        )


"""     def serialize(self):
        return {
            "id" : self.id,
            "autor" : self.autor,
            "titulo" : self.titulo,
            "editorial" : self.editorial,
            "fecha_edicion": self.fecha_edicion,
            "lugar_edicion": self.lugar_edicion,
            "area": self.area
        }
 """

""" class Libros(db.Model):
    id = db.Column(db.Integer, nullable= False, primary_key=True)
    isbn = db.Column(db.String(20))
    tipo_texto=db.Column(db.String(30))
    titulo = db.Column(db.String(200), nullable=False)
    autor = db.Column(db.String(200), nullable=False)
    editorial = db.Column(db.String(200), nullable=False)
    fecha_edicion = db.Column(db.Integer)
    lugar_edicion = db.Column(db.String(100))
    materia = db.Column(db.String(200), nullable=False)
    fecha_alta = db.Column(db.String(10))
    estantes = db.Column(db.String(10))

    def __init__(self, id, isbn, tipo_texto,titulo, autor, editorial, fecha_edicion, lugar_edicion, materia, fecha_alta,estantes):
        super().__init__()
        self.id = id
        self.isbn = isbn
        self.tipo_texto = tipo_texto
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.fecha_edicion = fecha_edicion
        self.lugar_edicion = lugar_edicion
        self.materia = materia
        self.fecha_alta = fecha_alta
        self.estantes= estantes """
