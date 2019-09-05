from flask import Flask, render_template, redirect, url_for, request, session 

import os
import shelve

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
	if request.method == 'POST':
		db= shelve.open('datos.dat')
		session['nombre'] = request.form['nombre']
		#Insertar datos en disco
		db[session['nombre']]= session['nombre']
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

	if 'nombre' in session:
		nombre = db[session['nombre']]
	else:
		nombre = None

	return render_template("datos.html", nombre = nombre, titulo='Informacion', eslogan='La pagina donde te sera facil conocer gente!', correo='hi5@correo.com',direccion='C/ Hospitalet de Lobregat s/n telefono: 9525552155')

@app.route('/fotos')
def fotos():

        if 'nombre' in session:
                nombre = session['nombre']
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
                        'autor' : { 'nombre':'Alvaro'}
                }
        ]

        return render_template("fotos.html", nombre = nombre, posts=posts, titulo='Fotos', eslogan='La pagina donde te sera facil conocer gente!', correo='hi5@correo.com',direccion='C/ Hospitalet de Lobregat s/n telefono: 9525552155')


@app.route('/editar', methods=['GET','POST'])
def editar():

	if 'nombre' in session:
		nombre = db[session['nombre']]
#		if request.method == 'POST' and request.form[session['nombre']] != '' :
#			db[str(session['nombre'])]=str(request.form[session['nombre']])
#			nombre=db[session['nombre']]
	else:
		nombre = None

	return render_template("editar.html", nombre = nombre, titulo='Editar', eslogan='La pagina donde te sera facil conocer gente!', correo='hi5@correo.com',direccion='C/ Hospitalet de Lobregat s/n telefono: 9525552155')

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == '__main__':
	print ("")
	app.run(host='0.0.0.0', debug = True)

