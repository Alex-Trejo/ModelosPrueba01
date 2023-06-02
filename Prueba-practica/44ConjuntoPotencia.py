def conjunto_potencia(lista_conjuntos):
    conjunto_resultado = set()
    conjunto_resultado.add(frozenset())  # Agrega el conjunto vacío

    for conjunto in lista_conjuntos:
        nuevos_subconjuntos = set()

        for subconjunto in conjunto_resultado:
            nuevos_subconjuntos.add(subconjunto)
            nuevos_subconjuntos.add(subconjunto.union(conjunto))

        conjunto_resultado = nuevos_subconjuntos

    return conjunto_resultado


conjuntos = [{1, 2}, {3, 4, 5}, {6}]
resultado = conjunto_potencia(conjuntos)
print(resultado)
