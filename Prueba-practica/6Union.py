"""
Modelos discretos para Ingenieria en Software
Nombre: Alex Trejo
NRC:9714
Fecha: 31/5/2023

6.Realiza la operación de unión de dos conjuntos utilizando una 
lista en Python. Muestra el resultado por pantalla

"""

def leer_conjunto():
    conjunto = []
    elementos = input("Ingrese los elementos del conjunto separados por comas: ")
    elementos = elementos.split(",")
    for elemento in elementos:
        conjunto.append(elemento.strip())
    return conjunto

print("Ingrese los elementos del primer conjunto:")
conjunto1 = leer_conjunto()

print("Ingrese los elementos del segundo conjunto:")
conjunto2 = leer_conjunto()


unionOfSets=conjunto1 + conjunto2

print("Conjunto A:",conjunto1)
print("Conjunto B:",conjunto2)
print("Union de A y B:",unionOfSets)





