PESO = 1
VALOR = 0

def achar_solucao(capacidade, itens, i):
    #print(i)

    if i>=n:
        return 0

    if (itens[i][PESO] > capacidade):
        
        return achar_solucao(capacidade, itens, i+1)
    
    return max(itens[i][VALOR] + achar_solucao(capacidade - itens[i][PESO], itens, i+1), achar_solucao(capacidade, itens, i+1))

n = input()
n, w = map(int, n.split(' '))

itens = []
for i in range(n):
    
    valores = input()
    v, p = map(int, valores.split(' '))
    itens.append([v, p])


print(achar_solucao(w, itens, 0))