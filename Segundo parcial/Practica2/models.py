from main import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(50))
    nombre = db.Column(db.String(255), nullable=False)

class Proveedor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    razonSocial = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(50))
    direccion =  db.Column(db.String(255))
    
class Producto(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     descripcion = db.Column(db.String(300), nullable=False)
     precio = db.Column(db.Float, nullable=False)
     

