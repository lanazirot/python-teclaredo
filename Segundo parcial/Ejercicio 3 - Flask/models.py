from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(50))
    nombre = db.Column(db.String(255), nullable=False)
    rol = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)

class Proveedor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    razonSocial = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(50))
    direccion =  db.Column(db.String(255))
    productos = db.relationship("Producto", backref='proveedor', cascade="all,delete", lazy="dynamic")
    
    def __repr__(self):
        return f"{self.razonSocial} ({self.id})"
    
class Producto(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     descripcion = db.Column(db.String(300), nullable=False)
     precio = db.Column(db.Float, nullable=False)
     id_proveedor = db.Column(db.Integer, db.ForeignKey('proveedor.id'))

