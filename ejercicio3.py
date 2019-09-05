#-*- coding: utf-8 -*-#

from flask import Flask
app = Flask(__name__)

@app.route('/user/<username>')
def mostrarPerfilUsuario(username):
	return 'Hola %s' % username

@app.errorhandler(404)
def page_not_found(error):
	return "Pagina no encontrada", 404

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
