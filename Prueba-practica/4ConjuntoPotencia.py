"""
Modelos discretos para Ingenieria en Software
Nombre: Alex Trejo
NRC:9714
Fecha: 31/5/2023


Implementa una función en Python que reciba una lista de conjuntos 
y devuelva el conjunto potencia de dicha lista. Prueba la función con conjuntos de tu elección. 


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



def conjunto_potencia(lista_conjuntos):
    conjunto_resultado = set()
    conjunto_resultado.add(frozenset())  # Agrega el conjunto vacío

    for conjunto in lista_conjuntos:
        nuevos_subconjuntos = set()

        for subconjunto in conjunto_resultado:
            nuevos_subconjuntos.add(subconjunto)
            nuevos_subconjuntos.add(subconjunto + (conjunto))

        conjunto_resultado = nuevos_subconjuntos

    return conjunto_resultado


   

print("Ingrese los elementos del primer conjunto:")
conjunto1 = leer_conjunto()

resultado=conjunto_potencia(conjunto1)

print("Conjunto A:",conjunto1)






