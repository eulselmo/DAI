from flask import Flask, render_template 
app = Flask(__name__)

@app.route('/index')
def index():
	usuario = { 'nombre' : 'angel'}
	posts = [
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
	return render_template("index.html", usuario=usuario,  posts=posts, titulo='Hi5', eslogan='La pagina donde te sera facil conocer gente!', correo='hi5@correo.com',direccion='C/ Hospitalet de Lobregat s/n telefono: 9525552155')

@app.route('/portada')
def portada():
	return render_template('portada.html')

@app.route('/informacion')
def informacion():
	return render_template('informacion.html')

@app.route('/fotos')
def fotos():
	return render_template('fotos.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug = True)

