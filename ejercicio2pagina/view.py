from flask import Flask, render_template, redirect, url_for, request, session 

import os

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		session['nombre'] = request.form['nombre']
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


@app.route('/logout')
def logout():
	session.pop('nombre', None)
	return redirect(url_for('index'))

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug = True)

