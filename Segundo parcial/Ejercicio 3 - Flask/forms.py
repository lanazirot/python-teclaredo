from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from wtforms_sqlalchemy.fields import QuerySelectField
from models import Proveedor

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired()])
    enviar = SubmitField("Iniciar sesion")

class UserForm(FlaskForm):
    # Campos necesarios
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    nombre = StringField("Nombre", validators=[DataRequired()])
    rol = StringField("Rol", validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired()])
    
    # Boton para enviar datos.
    enviar = SubmitField("Enviar datos")

class ProveedorForm(FlaskForm):
    # Campos necesarios
    razonSocial = StringField("Razon social", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    direccion = StringField("Direccion", validators=[DataRequired()])
    
    # Boton para enviar datos.
    enviar = SubmitField("Enviar datos")


def proveedores():
    return Proveedor.query

class ProductoForm(FlaskForm):
    # Campos necesarios
    descripcion = StringField("Descripcion", validators=[DataRequired()])
    precio = StringField("Precio", validators=[DataRequired()])
    proveedor = QuerySelectField("Proveedor", query_factory=proveedores)
    
    # Boton para enviar datos.
    enviar = SubmitField("Enviar datos")