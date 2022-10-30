import logging
from flask import Flask, abort, request, url_for, render_template, redirect, session, flash
from database import db
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap5
from models import Producto, Proveedor, User
from forms import LoginForm
app = Flask(__name__)
bootstrap = Bootstrap5(app)

logging.basicConfig(filename='tienda_logger.log', level=logging.DEBUG)

# Configurar la db
USER_DB = 'postgres'
PASS_DB = 'admin'
URL_DB = 'localhost'
NAME_DB = 'tienda'
FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['BOOTSTRAP_BTN_STYLE'] = 'primary'
app.config['BOOTSTRAP_BTN_SIZE'] = 'sm'

db.init_app(app)


# Configurar migracion
migrate = Migrate()
migrate.init_app(app, db)


# Secret key
app.config['SECRET_KEY'] = "$db8384jndkJS38EXXUDE8RHDl"

## Middleware para revisar la sesion ##



## Rutas de sesion ##


@app.route("/", methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
@app.route("/login.html", methods=['GET', 'POST'])
@app.route("/login.html", methods=['GET', 'POST'])
def login():
    session.pop('_flashes', None)
    loginForm = LoginForm()
    if loginForm.validate_on_submit():
        username = loginForm.username.data
        password = loginForm.password.data
        user = User(password='123', username='lana')
        if not user:
            flash('Usuario no encontrado')
            return redirect(url_for('login'))
        if user.password == password:
            return redirect(url_for('inicio'))
        else:
            flash('Datos incorrectos')
            return redirect(url_for('login'))
        
    return render_template('/login/login.html',form=loginForm)


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
    proveedores = Proveedor.query.all()
    return render_template('/proveedor/index.html', proveedores=proveedores)

@app.route("/proveedores/<int:id>/productos")
def productosProveedor(id):
    proveedor = Proveedor.query.get_or_404(id)
    return render_template('/proveedor/productos.html', proveedor=proveedor)


# ## Fin rutas proveedores ##

## Rutas de usuarios ##
@app.route("/usuarios")
@app.route("/usuarios.html")
def usuarios():
    return render_template('/user/index.html')


# ## Fin rutas de usuarios ##

## Rutas de productos ##
@app.route("/productos")
@app.route("/productos.html")
def productos():
    return render_template('/producto/index.html')


# ## Fin rutas de usuarios ##


## Rutas default ##
@app.route("/inicio")
@app.route("/inicio.html")
def inicio():
    return render_template('/inicio/index.html')

# # Error handlers


@app.errorhandler(404)
def appErrorHandler(error):
    return render_template('/default/error.html', error=error), 404


@app.errorhandler(401)
def appErrorHandler(error):
    return render_template('/login/login.html', error=error), 401


# Comentarios

# Correr codigo = flask db init = crear carpetas proyecto
# Empezar migraciones = flask db migrate = crear tabla default
# Hacer migraciones = flask db upgrade = actualizar
# Instalar formas = pip install flask-wtf
