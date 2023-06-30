from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
import bcrypt

class Books(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    author = db.Column(db.String(200), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    editorial = db.Column(db.String(100), nullable=False)
    availability = db.Column(db.String(100), nullable=False)
    area = db.Column(db.String(50), nullable=False)
    admin_id = db.Column(db.Integer, db.ForeignKey('admins.id'))
    admin = db.relationship('Admins', backref='books')

    def __init__(self, author, title, editorial,area, availability):
        super().__init__()
        self.author = author
        self.title = title
        self.editorial = editorial
        self.availability = availability
        self.area = area

    def __str__(self):
        return "\nAutor: {}. Titulo: {}. Editorial: {}. Disponibilidad: {}. Área: {}\n".format(
            self.author,
            self.title,
            self.editorial,
            self.availability,
            self.area
        )
    
class Admins(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    def set_password(self, password):
        password_bytes = password.encode('utf-8')
        self.password_hash = bcrypt.hashpw(password_bytes, bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password):
        password_bytes = password.encode('utf-8')
        return bcrypt.checkpw(password_bytes, self.password_hash.encode('utf-8'))
        

    def __init__(self, name, password_hash=''):
        super().__init__()
        self.name = name
        self.password_hash = password_hash
        

    def __str__(self):
        return "\nName: {}. Password_hash: {}\n".format(
            self.name,
            self.password_hash,
            
        )


