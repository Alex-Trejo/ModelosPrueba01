"""
Modelos discretos para Ingenieria en Software
Nombre: Alex Trejo
NRC:9714
Fecha: 31/5/2023


3. Diseña un programa en Python que solicite al usuario ingresar 
dos conjuntos y muestre por pantalla si el primero es un subconjunto del segundo. 


"""
import random
import string



def leer_conjunto():
    conjunto = set()
    elementos = input("Ingrese los elementos del conjunto separados por comas: ")
    elementos = elementos.split(",")
    for elemento in elementos:
        conjunto.add(elemento.strip())
    return conjunto


    

print("Ingrese los elementos del primer conjunto:")
conjunto1 = leer_conjunto()

print("Ingrese los elementos del segundo conjunto:")
conjunto2 = leer_conjunto()

print("Conjunto A:",conjunto1)
print("Conjunto B:",conjunto2)

if conjunto1.issubset(conjunto2):
    print("El primer conjunto",'A',"es un subconjunto del segundo conjunto",'B')
else:
    print("El primer conjunto",'A'," no es un subconjunto del segundo",'B')


