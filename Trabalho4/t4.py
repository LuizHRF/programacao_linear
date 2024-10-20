from t4_aux import *
from pyscipopt import Model, quicksum

grafo = le_grafo('Trabalho4/instancias_conjunto_independente_maximo/2_johnson8-4-4.clq')

modelo = Model("Conjunto Independente Maximo")

modelo.setParam("presolving/maxrounds", 0)
modelo.setParam("separating/maxrounds", 0)

vars = [modelo.addVar(name=str(v), vtype="B") for v in range(1, grafo.vertices + 1)]

modelo.setObjective(quicksum(vars), sense="maximize")

cons = {}
for i in range(1, grafo.getVertices()):
    for v in grafo.adjacencia[i]:
        cons[i] = modelo.addCons(vars[v] + vars[i] <= 1)

modelo.optimize()

independet_set  = [v for v in range(1, grafo.getVertices()) if modelo.getVal(vars[v]) == 1]

print(len(independet_set))