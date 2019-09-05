from flask import Flask
from random import randint

app = Flask(__name__)

@app.route('/')
def main():
	numeroImagen=randint(1,3)
	numeroColor=randint(0,6)
	colores=["red","blue","green","brown","black","yellow","white"]
	color=colores[numeroColor]
	imagen=""

	if numeroImagen==1:
		lado1=randint(100, 400)
		lado2=randint(100, 400)
		imagen="<rect width="+ str(lado1) +" height="+ str(lado2) +" fill="+ color +" />"
	elif numeroImagen==2:
		radio=randint(10, 300)
		posicionx=randint(200, 400)
		posiciony=randint(100, 300)
		imagen="<circle cx="+ str(posicionx) +" cy="+ str(posiciony) +" r="+ str(radio) +" fill="+ color +" />"
	else:
		radio=randint(100, 200)
		posicionx=randint(200, 400)
		posiciony=randint(80, 200)
		radiox=randint(80, 200)
		radioy=randint(80, 200)
		imagen="<ellipse cx="+ str(posicionx) +" cy="+ str(posiciony) +" rx="+ str(radiox) +" ry="+ str(radioy) +" fill="+ color +" />"

	return """

        <html>

        <head>
                <meta http-equiv="content-type" content="charset=utf-8">
                <title>Ejercicio2</title>
        </head>

        <body style="background:grey;">
		<svg width="1000" height="1000">
			%s
		</svg>
	</body>

        </html>
"""% imagen

if __name__ == '__main__':
        app.run(host='0.0.0.0', debug=True)

