PESO = 1
VALOR = 0

from sys import setrecursionlimit

setrecursionlimit(2000)

def inicializa_matriz(n, w):

    matriz = []

    for i in range(n):
        matriz.append( [-1] * (w+1))
    
    return matriz

def achar_solucao(capacidade, itens, i, m):
    #print(i)

    if i>=n:
        return 0
    
    if m[i][capacidade] != -1:
        return m[i][capacidade]

    if (itens[i][PESO] > capacidade):
        
        m[i][capacidade] = achar_solucao(capacidade, itens, i+1, m)
        return m[i][capacidade]
        
    m[i][capacidade] = max(itens[i][VALOR] + achar_solucao(capacidade - itens[i][PESO], itens, i+1, m), achar_solucao(capacidade, itens, i+1, m))
    return m[i][capacidade]

n = input()
n, w = map(int, n.split(' '))

m = inicializa_matriz(n, w)

itens = []
for i in range(n):
    
    valores = input()
    v, p = map(int, valores.split(' '))
    itens.append([v, p])


print(achar_solucao(w, itens, 0, m))