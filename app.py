from flask import Flask, render_template, url_for , request, redirect
import requests
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/proyecto.db'
db = SQLAlchemy(app)
#clase para creacion de base de datos AR98
class Alumno(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)
    apellido = db.Column(db.String)
    numero = db.Column(db.Integer)
    ciudad = db.Column(db.String)
    departamento = db.Column(db.String)
    modalidad = db.Column(db.String)
    eleccion = db.Column(db.String)
class Maestro(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)
    apellido = db.Column(db.String)
    numero = db.Column(db.Integer)
    ciudad = db.Column(db.String)
    departamento = db.Column(db.String)
    modalidad = db.Column(db.String)
    eleccion = db.Column(db.String)


@app.route('/',methods=['GET','POST'])
def principal():
    if request.method == 'POST':
        nombre = request.form.get('username', None)
        contrasena = request.form.get('contrasenha', None)
        patronal = request.form.get("patronal", None)
        check= request.form.get("check", None)
        return redirect(url_for('home')) 
    return render_template('login.html')

class clase:
    def __init__(self,img,titulo,desc):
        self.img = img
        self.titulo = titulo
        self.desc = desc

# ruta de sebas




#funcion para devolver datos desde la base a la pagina seleccionada 
@app.route('/tarjetas')
def tarjeta():
    maestros = Maestro.query.all()
    return render_template('lista_de_artesanos.html', maestros=maestros)

# pagina de formulario ar98
@app.route("/formulario")
def admin():
    # return render_template("formulario.html")
    return render_template("registro.html")


# esta es la funcion que trae los datos ingresados en el formulario y lo guarda en la base de datoss
@app.route("/data", methods= [ 'GET' , 'POST']) #metodo post es el que perimete el guardado de los datos en la BD
def carga():
    intento_de_leer = request.form['eleccion']
    if intento_de_leer=="2":
        tarea = Alumno(
        nombre=request.form['nombre'],
        apellido=request.form['apellido'],
        numero=request.form['numero'],
        ciudad=request.form['ciudad'],
        departamento=request.form['departamento'],
        modalidad=request.form['tecnica'],
        eleccion=request.form['eleccion'] #CAMBIAR VARIABLE A MODALIDAD
        )
        db.session.add(tarea)
        db.session.commit()
        return redirect(url_for('home'))
        # return redirect(url_for('admin'))
    elif intento_de_leer=="1":
        tarea = Maestro(
        nombre=request.form['nombre'],
        apellido=request.form['apellido'],
        numero=request.form['numero'],
        ciudad=request.form['ciudad'],
        departamento=request.form['departamento'],
        modalidad=request.form['tecnica'],
        eleccion=request.form['eleccion'] #CAMBIAR VARIABLE A MODALIDAD
        )
        db.session.add(tarea)
        db.session.commit()
        return redirect(url_for('home'))
        # return redirect(url_for('admin'))


@app.route("/home",methods=['GET'])
def home():
    lista_clases = []
    lista_clases.append(clase('clase5.png','Arte en Tela','''Todo lo que ves lo puedes alcanzar, recuerda que 
el arte sobre tela es complicado, pero no imposible
con los tips que te brindamos podras............'''))
    lista_clases.append(clase('clase1.png','Introducción a tallado en madera','''De la mano de nuestro gran artista, llega este curso
con todo lo que necesitas saber para integrarte en 
el hermoso mundo del tallado......'''))
    lista_clases.append(clase('clase2.png','El arte del Filigrama','''Filigrana una técnica milenaria que consiste 
en unir hilos finos que conforman elaboradas
piezas de joyería y orfebrería formando singulares
dibujos y diseños. Toda la información que 
necesitas esta aqui......'''))
    lista_clases.append(clase('clase3.png','El karanday nos llama','''El karanday es uno de los objetos más 
representativos del trabajo manual de nuestros 
compatriotas, aqui puedes encontrar toda la
informacion paso a paso. ....'''))
    lista_clases.append(clase('clase4.png','Introducción al moldeado en barro','''Los cántaros, que se fabrican con metal o con 
barro, suelen tener asas o manijas. En esta ocasión
aprenderas el arte del barro y podras.........'''))
    
    #cargar mas de la foto de ellos y agregar el texto de figma
    return render_template('index.html',clases=lista_clases)

@app.route("/info",methods=['GET'])
def info():
    
    return render_template('info.html')

@app.route('/guia')
def guia_principal():
    return render_template('wikihow.html')