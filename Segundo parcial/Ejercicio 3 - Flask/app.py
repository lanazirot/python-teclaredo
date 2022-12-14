import logging
from flask import Flask, abort, request, url_for, render_template, redirect, session, flash
from database import db
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap5
from models import Producto, Proveedor, User
from forms import LoginForm, ProveedorForm, ProductoForm, UserForm
from flask_wtf.csrf import CSRFProtect

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

csrf = CSRFProtect()
csrf.init_app(app)

# Secret key
app.config['SECRET_KEY'] = "$db8384jndkJS38EXXUDE8RHDl"

## Rutas de sesion ##

@app.before_request
def middleware():
    login_url = url_for('login')
    if request.path == login_url:
        return
    elif not session.get('logged_in', False):
        return redirect(login_url)
    

@app.route("/", methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
def login():
    if session.get('logged_in', False):
        return redirect(url_for('inicio'))
    loginForm = LoginForm()
    if loginForm.validate_on_submit():
        username = loginForm.username.data
        password = loginForm.password.data
        user = User.query.filter_by(username=username).first()
        if not user:
            return redirect(url_for('login'))
        if user.password == password:
            session['logged_in'] = True
            return redirect(url_for('inicio'))
        else:
            return redirect(url_for('login'))
        
    return render_template('/login/login.html',form=loginForm)


@app.route('/logout')
def logout():
    if session:
        session.pop('logged_in')
    return redirect(url_for('login'))
## Fin rutas de sesion ##


## Rutas de proveedores ##
@app.route("/proveedores")
def proveedores():
    proveedores = Proveedor.query.all()
    return render_template('/proveedor/index.html', proveedores=proveedores)

@app.route("/proveedores/<int:id>/productos")
def productosProveedor(id):
    proveedor = Proveedor.query.get_or_404(id)
    return render_template('/proveedor/productos.html', proveedor=proveedor)

@app.route("/proveedores/agregar", methods=['GET', 'POST'])
def agregarProveedor():
    proveedor = Proveedor()
    personaForm = ProveedorForm(obj=proveedor)
    if request.method == 'POST':
        if personaForm.validate_on_submit():
            personaForm.populate_obj(proveedor)
            # Insert a la db
            db.session.add(proveedor)
            db.session.commit()
            return redirect(url_for('proveedores'))
    return render_template('/proveedor/agregar.html', forma = personaForm)

@app.route("/proveedores/<int:id>/editar", methods=['GET', 'POST'])
def editarProveedor(id):
    proveedor = Proveedor.query.get_or_404(id)
    personaForm = ProveedorForm(obj=proveedor)
    if request.method == 'POST':
        if personaForm.validate_on_submit():
            personaForm.populate_obj(proveedor)
            #Update a la db, no es necesario hacer nada mas.
            db.session.commit()
            return redirect(url_for('proveedores'))
    return render_template('/proveedor/edit.html', forma = personaForm)

@app.route("/proveedores/<int:id>/eliminar")
def eliminarProveedor(id):
    proveedor = Proveedor.query.get_or_404(id)
    db.session.delete(proveedor)
    db.session.commit()
    return redirect(url_for('proveedores'))


# ## Fin rutas proveedores ##

## Rutas de usuarios TODO: Hacer con peticiones HTTP  ##
@app.route("/usuarios")
def usuarios():
    usuarios = User.query.all()
    return render_template('/user/index.html', usuarios=usuarios)

@app.route("/usuarios/agregar", methods=['GET', 'POST'])
def agregarUsuario():
    if request.method == 'POST':
        data = request.form
        # Obteniendo los datos de la peticion HTTP
        user = User(username=data['username'], password=data['password'], nombre=data['nombre'], email=data['email'], rol=data['rol'])
        userForm = UserForm(obj=user)
        if userForm.validate():
            db.session.add(user)
            db.session.commit()
            
        return redirect(url_for('usuarios'))
    return render_template('/user/agregar.html')

@app.route("/usuarios/<int:id>/editar", methods=['GET', 'POST'])
def editarUsuario(id):
    user = User.query.get_or_404(id)
    if request.method == 'POST':
        data = request.form
        # Obteniendo los datos de la peticion HTTP
        user.username = data['username']
        user.nombre = data['nombre']
        user.email = data['email']
        user.rol = data['rol']
        db.session.commit()
        return redirect(url_for('usuarios'))
    return render_template('/user/edit.html', usuario = user )

@app.route("/usuarios/<int:id>/eliminar")
def eliminarUsuario(id):
    usuario = User.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    return redirect(url_for('usuarios'))

# ## Fin rutas de usuarios ##

## Rutas de productos ##

@app.route("/productos")
def productos():
    productos = Producto.query.all()
    return render_template('/producto/index.html', productos=productos)

@app.route("/productos/agregar", methods=['GET', 'POST'])
def agregarProducto():
    producto = Producto()
    productoForm = ProductoForm(obj=producto)
    if request.method == 'POST':
        if productoForm.validate_on_submit():
            productoForm.populate_obj(producto)
            # Insert a la db
            db.session.add(producto)
            db.session.commit()
            return redirect(url_for('productos'))
    return render_template('/producto/agregar.html', forma = productoForm)

@app.route("/producto/<int:id>/editar", methods=['GET', 'POST'])
def editarProducto(id):
    producto = Producto.query.get_or_404(id)
    productoForm = ProductoForm(obj=producto)
    if request.method == 'POST':
        if productoForm.validate_on_submit():
            productoForm.populate_obj(producto)
            #Update a la db, no es necesario hacer nada mas.
            db.session.commit()
            return redirect(url_for('productos'))
    return render_template('/producto/edit.html', forma = productoForm)

@app.route("/producto/<int:id>/eliminar")
def eliminarProducto(id):
    producto = Producto.query.get_or_404(id)
    db.session.delete(producto)
    db.session.commit()
    return redirect(url_for('productos'))




# ## Fin rutas de productos ##


## Rutas default ##
@app.route("/inicio")
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
