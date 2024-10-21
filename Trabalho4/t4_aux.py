# =======================================================
# Trabalho 4 - Programação Linear
# Alunos: Luiz Faccio e Robert Drey
# =======================================================
# Este script contém funções auxiliares para a resolução
# das instâncias do problema.
# =======================================================


class Grafo:
    def __init__(self):
        self.adjacencia = {}
        self.vertices = 0

    def getVertices(self):
        return self.vertices

    def set_vertices(self, vertices):
        self.vertices = vertices + 1
        self.adjacencia = {i: set() for i in range(1, vertices + 1)}

    def add_aresta(self, aresta):
        u, v = aresta
        self.adjacencia[u].add(v)
        self.adjacencia[v].add(u)

    def print(self):
        print(f"Número de vértices: {self.vertices}")
        print("Lista de adjacência:")
        for vertice, vizinhos in self.adjacencia.items():
            print(f"{vertice}: {sorted(vizinhos)}")

def le_grafo(path):
    with open(path, 'r') as f:
        g = Grafo()
        linhas = f.readlines()
        for linha in linhas:
            l = linha.split(" ")
            match l[0]:
                case 'c':
                    pass
                case 'p':
                    g.set_vertices(int(l[2]))
                case 'e':
                    g.add_aresta((int(l[1]), int(l[2])))
                case _:
                    pass
    return g

def GeraClique(grafo, v):
    adjacencia = grafo.adjacencia

    Q = {v}.union(adjacencia[v])

    for u in list(Q):
        if u == v:
            continue
        
        vizinhos = False
        for w in Q:
            if w != u:  
                if w not in adjacencia[u]:  
                    vizinhos = True
                    break
        
        if vizinhos:
            Q.remove(u)

    return Q