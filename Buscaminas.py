from random import randint

def imprimirMatriz(matriz):
    for col in range(1,len(matriz[0])-1):
        print(col, end='\t')
    print()

    for fila in range(1,len(matriz)-1):
        for colm in range(1,len(matriz[0])-1):
            print(matriz[fila][colm],end='\t')
        #print(*matriz[fila], fila+1, sep = '\t')
        print(fila)
    print()

def crearMatrizVacia(filas,columnas,neutro):
    matriz = [[neutro]]*filas
    for pos in range(len(matriz)):
        matriz[pos] = matriz[pos] * columnas

    return matriz

def insertarMinas(filas, columnas, minas, MatrizBuscaminas):
    minas_puestas = 0

    while(True):
        for i in range(1,filas-1):
            for j in range(1,columnas-1):
                if minas_puestas < minas:
                    MatrizBuscaminas[i][j] = 9
                    minas_puestas += 1
                    continue
                return MatrizBuscaminas

def barajarMatriz(filas, columnas, MatrizBuscaminas):
    contador_barajadas = 0
    max_barajadas = 100000

    while contador_barajadas < max_barajadas:
        fOrigen = randint(1,filas - 2)
        fDestino = randint(1, filas - 2)
        cOrigen = randint(1,columnas - 2)
        cDestino = randint(1, columnas - 2)

        if fOrigen != fDestino or cOrigen != cDestino:
            MatrizBuscaminas[fOrigen][cOrigen] ^= MatrizBuscaminas[fDestino][cDestino] # 5 y 7 - 2
            MatrizBuscaminas[fDestino][cDestino] ^= MatrizBuscaminas[fOrigen][cOrigen] # 2 y 5 --> 7
            MatrizBuscaminas[fOrigen][cOrigen] ^= MatrizBuscaminas[fDestino][cDestino] # 2 y 7 --> 5

        contador_barajadas += 1

    return MatrizBuscaminas

def consultarVecindario(posI, posJ, MatrizBuscaminas):
    suma_vecindario = 0
    vecindario = 1

    for i in range(posI - vecindario,posI + vecindario + 1):
        for j in range(posJ - vecindario, posJ + vecindario + 1):
            if i != posI or j != posJ:
                suma_vecindario += MatrizBuscaminas[i][j] // 9

    return suma_vecindario

def llenarProximidad(MatrizBuscaminas):
    for i in range(1,len(MatrizBuscaminas)-1):
        for j in range(1,len(MatrizBuscaminas[0])-1):
            if MatrizBuscaminas[i][j] < 9:
                MatrizBuscaminas[i][j] = consultarVecindario(i, j, MatrizBuscaminas)
    return MatrizBuscaminas

def estaEnBorde(posX, posY,total_filas,total_columnas):
    return posX <= 0 or posY <= 0 or posX >= total_filas-1 or posY >= total_columnas-1

def revelarMatriz(fila, columna, MatrizBuscaminas,MatrizVisibilidad):
    if not estaEnBorde(fila, columna,len(MatrizBuscaminas),len(MatrizBuscaminas[0])):
        if MatrizVisibilidad[fila][columna] != 'X' or MatrizBuscaminas[fila][columna] > 0:
            MatrizVisibilidad[fila][columna] = MatrizBuscaminas[fila][columna]
            return MatrizVisibilidad
        else:
            MatrizVisibilidad[fila][columna] = MatrizBuscaminas[fila][columna]
            MatrizVisibilidad = revelarMatriz(fila - 1, columna, MatrizBuscaminas, MatrizVisibilidad)
            MatrizVisibilidad = revelarMatriz(fila, columna - 1, MatrizBuscaminas, MatrizVisibilidad)
            MatrizVisibilidad = revelarMatriz(fila, columna + 1, MatrizBuscaminas, MatrizVisibilidad)
            MatrizVisibilidad = revelarMatriz(fila + 1, columna, MatrizBuscaminas, MatrizVisibilidad)
            return MatrizVisibilidad
    return MatrizVisibilidad

def chequearGane(minas_encontradas,MatrizBuscaminas):
    valor_posiciones = 0

    for posicion_mina in minas_encontradas:
        x = posicion_mina[0]
        y = posicion_mina[1]
        valor_posiciones += MatrizBuscaminas[x][y]

    return valor_posiciones // 9 == len(minas_encontradas)

def jugar(MatrizBuscaminas,MatrizVisibilidad,cantidad_minas):
    print("Bienvenido al Buscaminas!")
    imprimirMatriz(MatrizVisibilidad)
    minas_encontradas = []

    while True:
        fila, columna = map(int, input("Digite valores (fila, columna): ").split())
        opcion = int(input("¿Que desea hacer? 0: Marcar mina, 1: Revelar posicion "))

        if opcion:
            MatrizVisibilidad = revelarMatriz(fila, columna, MatrizBuscaminas,MatrizVisibilidad)
            imprimirMatriz(MatrizVisibilidad)
            if MatrizVisibilidad[fila][columna] < 9:
                print("Vamos bien! Siga jugando!")
                continue
            print("Lo lamento, exploto. Ponte trucha")
            break
        MatrizVisibilidad[fila][columna] = '¬'
        imprimirMatriz(MatrizVisibilidad)
        minas_encontradas.append([fila,columna])
        if len(minas_encontradas) == cantidad_minas:
            if chequearGane(minas_encontradas,MatrizBuscaminas):
                print("Felicidades, gano el juego!")
                break
            print("Alguna mina no está bien colocada")
    print("Gracias por Jugar")

###############################################

filas, columnas, minas = map(int, input("Digite los valores iniciales: ").split())
filas += 2
columnas += 2
MatrizBuscaminas = crearMatrizVacia(filas, columnas,0)
MatrizVisibilidad = crearMatrizVacia(filas, columnas,'X')

#imprimirMatriz(MatrizBuscaminas)
MatrizBuscaminas = insertarMinas(filas, columnas, minas, MatrizBuscaminas)

#imprimirMatriz(MatrizBuscaminas)
MatrizBuscaminas = barajarMatriz(filas, columnas, MatrizBuscaminas)
#imprimirMatriz(MatrizBuscaminas)

MatrizBuscaminas = llenarProximidad(MatrizBuscaminas)
#imprimirMatriz(MatrizBuscaminas)

jugar(MatrizBuscaminas,MatrizVisibilidad,minas)