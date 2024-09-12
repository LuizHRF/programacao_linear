class retangulo():
    
    def __init__ (self, id, x1, y1, x2, y2):
        self.id = id
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        
    def print(self):
        print("Retangulo: ", self.id)
        print("Canto Inferior Esquerdo: ", self.x1, " " , self.y1)
        print("Canto Superior Direito: ", self.x2, " ", self.y2)
        
    def sobrepoem(self, ret2):
        if self.x1 > ret2.x2 or self.x2 < ret2.x1 or self.y1 > ret2.y2 or self.y2 < ret2.y1:
            return False
        return True

def leProblema(instancia):
    
    caminho = f"Trabalho2/trabalho_2/instancias_problema_rotulos/inst{instancia}.in"
    problema = open(caminho, "r")
    
    retangulos = []
    linhas = problema.readlines()
    
    num_rotulos = int(linhas[0])
    
    for i in range(1, num_rotulos+1):
        
        linha = linhas[i].split()
        retangulos.append(retangulo(i, float(linha[1]), float(linha[2]), float(linha[3]), float(linha[4])))
        
    return retangulos, num_rotulos