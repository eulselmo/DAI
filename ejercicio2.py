from flask import Flask
app = Flask(__name__)

@app.route('/')
def pagina():
	return """

	<html>

	<head>
		<meta http-equiv="content-type" content="charset=utf-8">
		<title>Ejercicio2</title>
	</head>

	<body style="background:grey;">
		<h2 style="color:blue;" align="center">Bienvenido a la pagina</h2>
		<img src="http://www.villalaangostura.com.ar/GaleriaFotos/imgs/galerias/Foto_31352758.jpg" width="200" height="200" align="right">
		<img src="http://www.villalaangostura.com.ar/GaleriaFotos/imgs/galerias/Foto_31352758.jpg" width="200" height="200" align="left">	
	</body>

	</html>
"""

if __name__ == '__main__':
        app.run(host='0.0.0.0', debug=True)

