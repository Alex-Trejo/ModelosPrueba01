"""
Modelos discretos para Ingenieria en Software
Nombre: Alex Trejo
NRC:9714
Fecha: 31/5/2023

1. Escribe un programa en Python que determine la intersección de dos 
conjuntos ingresados por el usuario. Muestra el resultado por pantalla. 


"""

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
interseccion = conjunto1.intersection(conjunto2)

print("Conjunto A: ",conjunto1)
print("Conjunto B: ",conjunto2)



print("La intersección de los conjuntos es: ", interseccion)

