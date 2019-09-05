from flask import Flask 
app = Flask(__name__)

@app.route('/index')
def index():
	return render_template('index.html')

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
