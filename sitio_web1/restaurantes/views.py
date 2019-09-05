from flask import Flask, render_template, redirect, url_for, request, session, jsonify 
from pymongo import MongoClient
from django.shortcuts import render, HttpResponse
from .models import restaurantes
from .forms import RestauranteForm
from .forms import BuscarForm

import os
import shelve
import json
from bson.json_util import dumps
client= MongoClient('mongodb://localhost:27017/')

app = Flask(__name__)

def get_name(request):
	if request.method=='POST':

		form=NameForm(request.POST)
		if form.is_valid():
			return render(request, 'printName.html', {'name':form.cleaned_data['your_name']})
	else:
		form=NameForm()

	return render(request, 'name.html', {'form':form})

def test_template(request):
	iterador= restaurantes.find().limit(10)
	context= {
	"lista": list(iterador)
	}
	return render(request,'test.html', context)

def index(request):

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
	return render(request, "index.html", {'posts':posts, 'titulo':'Hi5', 'eslogan':'La pagina donde te sera facil conocer gente!', 'correo':'hi5@correo.com','direccion':'C/ Hospitalet de Lobregat s/n telefono: 9525552155'})

#def grafica(request):

#	numero=busqueda_grafica()

#	return render(request, "grafica.html",{'datos':numero})

def datos(request):

	#if 'nombre' and 'contrasenia' in session:
	#	db= shelve.open('datos.dat')
	#	nombre = db[session['nombre']]
	#	db.close()
	#else:
	#	nombre = None

	return render(request, "datos.html", {'titulo':'Informacion', 'eslogan':'La pagina donde te sera facil conocer gente!', 'correo':'hi5@correo.com','direccion':'C/ Hospitalet de Lobregat s/n telefono: 9525552155'})

def fotos(request):

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

	return render(request, "fotos.html", {'posts':posts, 'titulo':'Fotos', 'eslogan':'La pagina donde te sera facil conocer gente!', 'correo':'hi5@correo.com','direccion':'C/ Hospitalet de Lobregat s/n telefono: 9525552155'})


def editar(request):

	return render(request, "editar.html", {'titulo':'Editar', 'eslogan':'La pagina donde te sera facil conocer gente!', 'correo':'hi5@correo.com','direccion':'C/ Hospitalet de Lobregat s/n telefono: 9525552155'})


def buscar(request):
#	if request.method == 'POST':
#		cocina=request.form['name']
#		resultados=busqueda_bd(cocina, 0)
#		return render(request, "buscar.html", {'valor':cocina,  'lista':resultados,  'nombre': nombre})
#
#	return render(request, "buscar.html", {'titulo':'Hi5', 'eslogan':'La pagina donde te sera facil conocer gente!', 'correo':'hi5@correo.com','direccion':'C/ Hospitalet de  Lobregat s/n telefono: 9525552155'})
	form = BuscarForm()
	if request.method =='POST':
		form=BuscarForm(request.POST)
		if form.is_valid():
			datos=form.cleaned_data
			resultados=busqueda_bd(datos['buscar'], 0)
			return render(request, 'buscar.html',{'valor':datos,'lista':resultados, 'form':form})

	context = {
		'form': form,
	}

	return render(request, 'buscar.html', context)


def get_datos():
	cocina = request.args.get('valor','')
	pag = int(request.args.get('pag',''))
	if pag<0:
		pag=0
	print(cocina)
	print(pag)
	#busqueda = buscar(informacion, num)
	resultados=busqueda_bd(cocina, pag)
	return dumps(resultados)

def busqueda_bd(cocina, pag):
	res_pag=15
        #Creamos la base de datos
	db = client.test
        #Colección de los restaurantes
	restaurants=db.restaurants
	lista=[]
        #Realizamos el find de los datos que se han introducido
	restaurantes=restaurants.find({'cuisine': cocina}).skip(res_pag*pag).limit(res_pag)

	for restaurante in restaurantes:
		print(restaurante['name'])
		datos={'nombre': restaurante['name'], 'tipo': restaurante['cuisine'], 'direccion': restaurante['address']['street'],'coordenadas':restaurante['address']['coord'],'mapa0':restaurante['address']['coord'][0], 'mapa1':restaurante['address']['coord'][1],'id':restaurante['restaurant_id']}
		lista.append(datos)
	return lista

def grafica(request):
	db = client.test
	restaurants=db.restaurants
	nrestaurante1=restaurants.find({'cuisine':'Bakery'}).count()
	print(nrestaurante1)
	nrestaurante2=restaurants.find({'cuisine':'patatas'}).count()
	print(nrestaurante2)
	#for i in restaurantes:
	return render(request,'grafica.html',{'datos1':nrestaurante1,'datos2':nrestaurante2})
def aniadir(datos):
	res_pag=15
        #Creamos la base de datos
	db = client.test
        #Colección de los restaurantes
	restaurants=db.restaurants
	#Insertamos
	restaurantes=restaurants.insert(   {
      "address" : {
         "street" : "",
         "zipcode" : datos['zipcode'],
         "building" : "",
         "coord" : ["",""]
      },
      "borough" : "",
      "cuisine" : datos['cuisine'],
      "grades" : [
         {
            "date" : "",
            "grade" : "",
            "score" : ""
         },
         {
            "date" : "",
            "grade" : "",
            "score" : ""
         }
      ],
      "name" : datos['name'],
      "restaurant_id" : ""
	})


def nuevo_restaurante(request):

	form = RestauranteForm()
	if request.method =='POST':
		form=RestauranteForm(request.POST)
		if form.is_valid():
			datos=form.cleaned_data
			aniadir(datos)
			return render(request, 'registro.html')

		else:
			print(form.errors)
	context = {
		'form': form,
	}
	return render(request, 'introducir.html', context)

def logout():
	session.pop('nombre', None)
	session.pop('contrasenia', None)
	return redirect(url_for('index'))

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == '__main__':
	print ("")
	app.run(host='0.0.0.0', debug = True)

