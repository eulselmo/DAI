from flask import Flask, request
from mandelbrot import renderizaMandelbrot
from mandelbrot import renderizaMandelbrotBonito
#import os

app = Flask(__name__)

@app.route('/pagina')
def pagina():

	x1= request.args.get('x1')
	y1= request.args.get('y1')
	x2= request.args.get('x2')
	y2= request.args.get('y2')
	tamano= request.args.get('tamano')
	iteraciones= request.args.get('iteraciones')
	paleta= eval(request.args.get('paleta'))
	total= x1 + y1 + x2 + y2 + tamano + iteraciones

	for i in paleta:
		total=total + str(i[0]) + str(i[1]) + str(i[2])

	nombreFichero="static/imagenes" + total + ".png"

	#if os.path.isfile(nombreFichero) == False:
	renderizaMandelbrotBonito(float(x1), float(y1), float(x2), float(y2), int(tamano), int(iteraciones), nombreFichero, paleta, len(paleta)) 
	return """

        <html>

        <head>
                <meta http-equiv="content-type" content="charset=utf-8">
                <title>Ejercicio2</title>
        </head>

        <body style="background:grey;">
                <img src="%s">
	</body>

	</html>

	"""% nombreFichero

if __name__ == '__main__':
        app.run(host='0.0.0.0', debug=True)

