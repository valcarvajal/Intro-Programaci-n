import sys
sys.setrecursionlimit(100000000)

#Modo 1
def Modo1(n,fac):
    if n==1:
        return 1
    if fac>n//2:
        return n
    if n%fac == 0:
        print(fac, end=' ')
        return Modo1(n//fac,fac) #se saca el n restante para seguirlo factorizando
    return Modo1(n,fac+1) #aumenta el factor


#Modo2
def Modo2(n):
    fac = 2
    while n!=1:
        if fac > n // 2:
            return n
        if n % fac == 0:
            n = (n // fac) #se cambia el valor de n para seguirlo factorizando
            print(fac, end=' ')
            continue
        fac += 1
    return 1


#Modo3
def Modo3(n,fac):
    if n == 1:
        return 1
    if fac*fac > n:
        return n
    if n % fac == 0:
        print(fac, end=' ') #se imprime para que de todos los factores y no solo el último
        return Modo1(n // fac, fac)
    return Modo1(n, fac + 2)


#Modo4
def Modo4(n):
    fac = 2
    while n!=1:
        if fac*fac > n:
            return n
        if n % fac == 0:
            n = (n // fac) #se cambia el valor de n al restante para seguirlo factorizando
            print(fac, end=' ') #se imprime para que de todos los factores y no solo el último
            continue
        fac += 1 #aumenta el factor
    return 1


#Modo5
def criba_eratostenes(n): #criba
    primos = []
    noPrimos = []

    for i in range(2, n + 1):
        if i not in noPrimos:
            primos.append(i)

        for k in range(i * i, n + 1, i): #i*i - raíz
            noPrimos.append(k)

    return primos #no ocupamos la otra lista, entonces solo retorna los primos

criba = criba_eratostenes(n) #es necesario definir el n aquí también para que funcione

def Modo5(n): #factorización con la criba
    global criba
    i = 0 #posición de la lista (Criba)
    factores = []
    while n != 1:
        if (criba[i]*criba[i] > n):
            return factores + [n] #agrega n a los factores
        if (n % criba[i] == 0):
            factores.append(criba[i])
            n //= criba[i] #se saca el restante de n para seguir factorizando
        else:
            i += 1  #aumenta para probar con el siguiente primo
    return "".join(str(factores))

#Definir n en el print y arriba en el modo 5
print(Modo1(n,2)) #se define fac como 2 para que inicie a partir de este número por ser el primer primo
print(Modo2(n))
print(Modo3(n, 2)) #se define fac como 2 para que inicie a partir de este número por ser el primer primo
print(Modo4(n))
print(Modo5(n))