from pulp import *
from T2_aux import *
import itertools

retangulos, num_rotulos = leProblema(instancia = 3)

modelo = LpProblem("Problema do Rotulos - Instancia 1", LpMaximize) #Modelo

x = LpVariable.dicts("x", range(1, (num_rotulos + 1)), 0, 1, LpInteger)  #Variáveis

modelo += (lpSum([x[i] for i in range(1, (num_rotulos + 1))]), "Funcao objetivo") #Função objetivo

pares_de_retangulos = itertools.combinations(retangulos, 2)
count = 0

for ret1, ret2 in pares_de_retangulos:  #Adicionando restrições de sobreposição
    #print("Testando sobreposicao entre retangulos ", ret1.id, " e ", ret2.id)
    if ret1.sobrepoem(ret2):
        modelo += (x[ret1.id] + x[ret2.id] <= 1, f"Restricao de Sobreposicao [{count}]")
        count += 1

modelo.solve()

for x in modelo.variables():
    if int(x.value()) == 1:
        print(x.name)
print("Valor otimo:", value(modelo.objective))

