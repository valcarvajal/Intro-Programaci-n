def crearMatrizVacia(filas,columnas):
    matriz_nueva = [[0]] * filas
    for posFila in range(filas):
        matriz_nueva[posFila] = matriz_nueva[posFila] * columnas
    return matriz_nueva

def imprimirMatriz(matriz):
    for fila in matriz:
        print(fila)
    print()

def sumaFila(fila):
    suma = 0
    for valor in fila:
        suma += valor
    return suma > 0

def sumaDiagonales(tablero,posI,posJ):
    suma = 0
    for j in range(1, posJ + 1):
        if(posI - j >= 0):
            suma += tablero[posI - j][posJ - j]
        if(posI + j < len(tablero)):
            suma += tablero[posI + j][posJ - j]
    return suma > 0

def puedoMeterReina(tablero,posI,posJ):
    SF = sumaFila(tablero[posI]) # Esto va a revisar si en esa fila hay un valor > 0
    SD = sumaDiagonales(tablero,posI,posJ) # Esto va a revisar si en las diagonales hay un valor > 0
    if not (SF + SD):
        tablero[posI][posJ] = 1
        return tablero
    return []

def sumaColumna(matriz,posCol):
    suma = 0
    for i in range(len(matriz)):
        suma += matriz[i][posCol]
    return suma

def calcularHijos(tablero):
    lista_hijos = []
    for j in range(len(tablero)):
        if (not sumaColumna(tablero,j)):
            for i in range(len(tablero)):
                matriz_nueva = [fila[:] for fila in tablero]
                resultado = puedoMeterReina(matriz_nueva,i,j)
                if resultado != []:
                    lista_hijos.append(resultado)
            return lista_hijos

def calcularSolucionesPila(tablero):
    pila = []
    pila.append(tablero)

    soluciones = []

    while (pila != []):
        top = pila.pop()
        if (sumaColumna(top,-1)):
            soluciones.append(top)
        else:
            hijos = calcularHijos(top)
            for posHoja in range(len(hijos),0,-1):
                pila.append(hijos[posHoja-1])
    return soluciones

########

n = int(input("Digite el n: "))

tablero = crearMatrizVacia(n,n)

soluciones = calcularSolucionesPila(tablero)

print("Encontramos {} soluciones!".format(len(soluciones)))
for solucion in soluciones:
    imprimirMatriz(solucion)
