
class Grafo():

    def __init__(self):
        self.vertices = 0
        self.arestas = []

    def set_vertices(self, vertices):
        self.vertices = vertices

    def add_aresta(self, aresta):
        self.arestas.append(aresta)

    def print(self):
        print(self.vertices)
        for aresta in self.arestas:
            print(f'[{aresta[0]} - {aresta[1]}]')

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
                    pass
                case 'e':
                    g.add_aresta((int(l[1]), int(l[2])))
                    pass
                case _:
                    pass
    return g         