from math import pow
from math import sqrt

def distanciaEuclidiana(vector1, vector2):
    distancia = 0.0

    for i in range(len(vector1)):
        distancia += pow(vector1[i] - vector2[i], 2)
    return sqrt(distancia)

def quicksort(matriz):
    if len(matriz) < 2:
        return matriz

    menores = []
    mayores = []
    pivote = matriz[-1]

    for pos in range(len(matriz[:-1])):
        if matriz[pos][1] >= pivote[1]: mayores.append(matriz[pos])
        else: menores.append(matriz[pos])
    return quicksort(menores) + [pivote] + quicksort(mayores)

def obtenerVecinos(lista_datos, caso_prueba):
    lista_distancias = []

    for vector in lista_datos:
        distancia = distanciaEuclidiana(vector[:-1], caso_prueba[:-1])
        lista_distancias.append([vector, distancia])
    listaOrdenada = quicksort(lista_distancias)
    return listaOrdenada


lista_datos = [[2.7810836, 2.550537003, 0]
               [1.465489372, 2.362125076, 0]
               [3.396561688, 4.400293529, 0]
               [1.38807019, 1.850220317, 0]
               [3.06407232, 3.005305973, 0]
               [7.627531214, 2.759262235, 1]
               [5.332441248, 2.088626775, 1]
               [6.922596716, 1.77106367, 1]
               [8.675418651, -0.242068655, 1]
               [7.673756466, 3.508563011, 1]]
prueba = [2.7810836, 2.550537003, 0]
obtenerVecinos(lista_datos, prueba)