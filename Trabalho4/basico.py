# =======================================================
# Trabalho 4 - Programação Linear
# Alunos: Luiz Faccio e Robert Drey
# =======================================================
# Este script executa, para uma instância do problema do 
# conjunto independente máximo, a solução para o modelo 
# matemático básico.
# =======================================================

from t4_aux import *
from pyscipopt import Model, quicksum

nome = "6_san200_0.7_1"
grafo = le_grafo(f'Trabalho4/instancias_conjunto_independente_maximo/{nome}.clq')

modelo = Model("Conjunto Independente Maximo")

modelo.setParam("presolving/maxrounds", 0)
modelo.setParam("separating/maxrounds", 0)

vars = [modelo.addVar(name=str(v), vtype="B") for v in range(1, grafo.vertices + 1)]

modelo.setObjective(quicksum(vars), sense="maximize")

cons = {}
counter = 0
for i in range(1, grafo.getVertices()):
    for v in grafo.adjacencia[i]:
        if v < i:
            counter += 1
            cons[counter] = modelo.addCons(vars[v] + vars[i] <= 1)
        
modelo.optimize()
modelo.writeProblem(filename=f"Trabalho4/Basico_{nome}.lp")


independet_set  = [v for v in range(1, grafo.getVertices()) if modelo.getVal(vars[v]) == 1]

print(len(independet_set))