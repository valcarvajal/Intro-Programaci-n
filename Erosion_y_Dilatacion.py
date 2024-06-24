from PIL import Image
import numpy as np

img = Image.open('foreground2.jpg').convert('1')
matriz = np.asarray(img)

########################################################################################
def interseccionMascara(pos_fila, pos_col, matriz, tamaño_mascara): #comprobando vecinos del pixel
    suma = 0
    for posFil in range(pos_fila - tamaño_mascara, pos_fila + tamaño_mascara):
        for posCol in range(pos_col - tamaño_mascara, pos_col + tamaño_mascara):
            suma += matriz[posFil][posCol]
    return suma

def erosion(matriz):
    tamaño_mascara = 3
    sensitividad = 5
    cant_filas = len(matriz)
    cant_cols = len(matriz[0])

    for pos_fila in range(tamaño_mascara // 2, cant_filas - tamaño_mascara // 2 - 1):
        for pos_col in range(tamaño_mascara // 2, cant_cols - tamaño_mascara // 2 - 1):
            interseccion = interseccionMascara(pos_fila, pos_col, matriz, tamaño_mascara) #cuantos pixeles vecindarios tienen valor de 1

            if interseccion <= sensitividad:
                matriz[pos_fila][pos_col] = 0

    return matriz

def dilatacion(matriz):
    tamaño_mascara = 3
    sensitividad = 5
    cant_filas = len(matriz)
    cant_cols = len(matriz[0])

   for pos_fila in range(tamaño_mascara // 2, cant_filas - tamaño_mascara // 2 - 1):
        for pos_col in range(tamaño_mascara // 2, cant_cols - tamaño_mascara // 2 - 1):
            interseccion = interseccionMascara(pos_fila, pos_col, matriz, tamaño_mascara)

            if interseccion >= sensitividad:
                matriz[pos_fila][pos_col] = 1

    return matriz


resultado1 = dilatacion(matriz)
matriz = erosion(matriz)

###################################################

imagen = Image.fromarray(matriz)
imagen.show()