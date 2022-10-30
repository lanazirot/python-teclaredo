import logging
from flask import Flask, abort, request, url_for, render_template, redirect, session
from database import db
from flask_migrate import Migrate
from models import Producto, Proveedor, User
app = Flask(__name__)

logging.basicConfig(filename='tienda_logger.log', level=logging.DEBUG)

#Configurar la db
USER_DB = 'postgres'
PASS_DB = 'admin'
URL_DB = 'localhost'
NAME_DB = 'tienda'
FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


#Configurar migracion
migrate = Migrate()
migrate.init_app(app,db)


# Secret key
app.config['SECRET_KEY'] = "$db8384jndkJS38EXXUDE8RHDl%"

## Middleware para revisar la sesion ##

@app.before_request()
def verificarSesion():
    if not session:
        return redirect(url_for('login'))

## Rutas de sesion ##
@app.route("/")
@app.route("/login")
@app.route("/login.html")
@app.route("/login.html")
def login():
    # Si ya tienes la sesion iniciada y tratas de ir al login, redirecciona al inicio
    if session and request.method == 'GET':
        return redirect(url_for('inicio'))
    if request.method == 'POST':
        usuario = request.form['username']
        usuarioModel = User.query.filter_by(username=usuario).first()
        if not usuarioModel:
            return abort(401)
        session['username'] = usuarioModel.username
        session['id'] = usuarioModel.id
        session['rol'] = usuarioModel.rol
        return redirect(url_for('inicio'))

@app.route('/logout')
def logout():
    if session:
        session.pop('username')
    return redirect(url_for('login'))
## Fin rutas de sesion ## 


## Rutas de proveedores ##
@app.route("/proveedores")
@app.route("/proveedores.html")
def proveedores():
    return render_template('/proveedor/index.html')


## Fin rutas proveedores ##

## Rutas de usuarios ##
@app.route("/usuarios")
@app.route("/usuarios.html")
def proveedores():
    return render_template('/user/index.html')


## Fin rutas de usuarios ##

## Rutas default ##
@app.route("/inicio")
@app.route("/inicio.html")
def inicio():
    isAdmin = session['rol'] == 'ADMIN'
    return render_template('/inicio/index.html', isAdmin=isAdmin)

## Error handlers
@app.errorhandler(404)
def appErrorHandler(error):
    return render_template('/default/error.html', error=error), 404

@app.errorhandler(401)
def appErrorHandler(error):
    return render_template('/login/login.html', error=error), 401


## Comentarios

## Correr codigo = flask db init = crear carpetas proyecto
## Empezar migraciones = flask db migrate = crear tabla default
## Hacer migraciones = flask db upgrade = actualizar
## Instalar formas = pip install flask-wtf