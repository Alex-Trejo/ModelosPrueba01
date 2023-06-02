"""
Modelos discretos para Ingenieria en Software
Nombre: Alex Trejo
NRC:9714
Fecha: 31/5/2023

Crea una función en Python que reciba dos conjuntos como parámetros y devuelva un nuevo conjunto que 
contenga los elementos presentes en el primer conjunto pero no en el segundo. Prueba la función 
con conjuntos de tu elección. 

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

def DiferenciaDeConjuntoAB(conjunto1, conjunto2):
    conjunto3 = conjunto1.copy()
    conjunto3.difference_update(conjunto2)
    return conjunto3
    

print("Ingrese los elementos del primer conjunto:")
conjunto1 = leer_conjunto()

print("Ingrese los elementos del segundo conjunto:")
conjunto2 = leer_conjunto()

conjunto3=DiferenciaDeConjuntoAB(conjunto1, conjunto2)

print("La diferencia de A - B:",conjunto3)













