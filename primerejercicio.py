#!/usr/bin/env python
#-*-coding:utf8-*-

from random import randrange

c=randrange(100)

print("Introduce un numero: ")

a=input()

def adivina(a):
	if a > c:
		print(a, 'Este numero es mayor que el numero buscado')

	elif a < c:
		print(a, 'Este numero es  menor que el numero buscado')

	else:
		print(a, 'Es igual al numero buscado')

for i in range(1,11):
	adivina(a)
	if a != c:
		print("Introduce de nuevo un numero: ")
		a=input()
	else:
		print("Has acertado")	
