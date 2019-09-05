from flask import Flask, render_template, redirect, url_for, request, session 

import os
import shelve

app = Flask(__name__)
#db= shelve.open('datos.dat', writeback=True)

@app.route('/login', methods=['POST'])
def login():
	if request.method == 'POST':
		db= shelve.open('datos.dat')
		session['nombre'] = request.form['nombre']
		#Insertar datos en disco
		db[session['nombre']]=str(request.form['contrasenia'])
		session['contrasenia']=request.form['contrasenia']
		db.close()
		return redirect(url_for('index'))


@app.route('/index')
def index():
	if 'nombre' in session:
		nombre = session['nombre']
	else:
		nombre = None

	posts= [
		{
			'autor' : { 'nombre':'Jacinto'},
			'texto' : 'Se acabo el descanso pre examenes, toca ponerse serios con...'
		},
		{
			'autor' : { 'nombre':'Rosa'},
			'texto' : 'Este es el segundo comentario'
		},
		{
			'autor' : { 'nombre':'Juan'},
			'texto' : 'Este es el tercer comentario'
		},
		{
			'autor' : { 'nombre':'Pepe'},
			'texto' : 'Este es el cuarto comentario'
		},
		{
                        'autor' : { 'nombre':'Angel'},
			'texto' : 'Este es el quinto comentario'
		},
		{
			'autor' : { 'nombre':'Alvaro'},
			'texto' : 'Este es el sexto comentario'
		}
	]
	return render_template("index.html", nombre = nombre,  posts=posts, titulo='Hi5', eslogan='La pagina donde te sera facil conocer gente!', correo='hi5@correo.com',direccion='C/ Hospitalet de Lobregat s/n telefono: 9525552155')

@app.route('/datos')
def datos():

	if 'nombre' and 'contrasenia' in session:
		db= shelve.open('datos.dat')
		nombre = db[session['nombre']]
		db.close()
	else:
		nombre = None

	return render_template("datos.html", nombre = nombre, contrasenia=session["contrasenia"] , titulo='Informacion', eslogan='La pagina donde te sera facil conocer gente!', correo='hi5@correo.com',direccion='C/ Hospitalet de Lobregat s/n telefono: 9525552155')

@app.route('/fotos')
def fotos():

	if 'nombre' in session:
		nombre = session['nombre']
		contrasenia = session['contrasenia']
	else:
                nombre = None

	posts= [
                {
                        'autor' : { 'nombre':'Jacinto'}
                },
                {
                        'autor' : { 'nombre':'Rosa'}
                },
                {
                        'autor' : { 'nombre':'Juan'}
                },
                {
                        'autor' : { 'nombre':'Pepe'}
                },
                {
                        'autor' : { 'nombre':'Angel'}
                },
                {
                        'autor' : { 'nombre':'Alvaro'}                }
        ]

	return render_template("fotos.html", nombre = nombre, posts=posts, titulo='Fotos', eslogan='La pagina donde te sera facil conocer gente!', correo='hi5@correo.com',direccion='C/ Hospitalet de Lobregat s/n telefono: 9525552155')


@app.route('/editar', methods=['GET','POST'])
def editar():

	if 'nombre' in session:
		db= shelve.open('datos.dat')
		nombre = session['nombre']
		if request.method == 'POST':
			session['contrasenia']=request.form['contrasenia']
			#contrasenia= session['contrasenia']
		else:
			contrasenia= session['contrasenia']
			nombre= session['nombre']
		db.close()
	else:
		nombre = None
		clave = None

	return render_template("editar.html", nombre = nombre, contrasenia=contrasenia, titulo='Editar', eslogan='La pagina donde te sera facil conocer gente!', correo='hi5@correo.com',direccion='C/ Hospitalet de Lobregat s/n telefono: 9525552155')

@app.route('/logout')
def logout():
	session.pop('nombre', None)
	session.pop('contrasenia', None)
	return redirect(url_for('index'))

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == '__main__':
	print ("")
	app.run(host='0.0.0.0', debug = True)

