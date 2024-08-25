from math import sqrt

class Nodo:

    def __init__(self, num, x_coord, y_coord):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.num = num

    def print(self):
        print("Nodo: ", self.num)
        print("Coordenada x: ", self.x_coord)
        print("Coordenada y: ", self.y_coord)

    def copy(self):
        return Nodo(self.num, self.x_coord, self.y_coord)
    

class Problem_info:
    def __init__(self, n, c, t, d, edg):
        self.name = n
        self.comment = c
        self.type = t
        self.dimension = d
        self.edge_weight_type = edg

    def print(self):
        print("Nome: ", self.name)
        print("Comentário: ", self.comment)
        print("Tipo: ", self.type)
        print("Dimensão: ", self.dimension)
        print("Tipo de peso da aresta: ", self.edge_weight_type)

##Função que calcula a distância entre dois nodos
def distancia(n1, n2):

    xd = n1.x_coord - n2.x_coord
    yd = n1.y_coord - n2.y_coord
    dij = (int) (sqrt(xd*xd + yd*yd) + 0.5)

    return dij

##Função que calcula o custo total de uma permutação
def custo_total(permutacao_final):
    
    custo = 0

    for i in range(len(permutacao_final)):

        if i == len(permutacao_final) - 1:
            custo += distancia(permutacao_final[i], permutacao_final[0])
        else:
            custo += distancia(permutacao_final[i], permutacao_final[i+1])

    return custo


##Função que lê o grafo do arquivo f
def ler_grafo(f):
    
    linhas = f.readlines()
    infos = []

    for i in range(5): 
        linha = linhas[i].split(':')
        infos.append(linha[1].strip())

    problema = Problem_info(infos[0], infos[1], infos[2], infos[3], infos[4])

    nodos = []

    for i in range(6, len(linhas)-1):

        linha = linhas[i].split()

        nodos.append(Nodo(num = int(linha[0]), x_coord= float(linha[1]), y_coord= float(linha[2])))

    return nodos, problema

def remove_nodo(lista, n):
    for nodo in lista:
        if nodo.num == n:
            lista.remove(nodo)
            return lista