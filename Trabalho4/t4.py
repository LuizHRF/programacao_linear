from t4_aux import *
from pyscipopt import Model

grafo = le_grafo('Trabalho4/instancias_conjunto_independente_maximo/2_johnson8-4-4.clq')

modelo = Model("Conjunto Independente Maximo")

modelo.setParam("presolving/maxrounds", 0)
modelo.setParam("separating/maxrounds", 0)

vars = {}
for v in range(1, grafo.vertices + 1):
    vars[v] = modelo.addVar(name=str(v), vtype="BINARY", obj=1)

for u in grafo.adjacencia:
    for v in grafo.adjacencia[u]:
        if u < v:  
            model.addCons(vars[u] + vars[v] <= 1)

model.optimize()
    
independent_set = [v for v in range(1, grafo.vertices + 1) if model.getVal(vars[v]) > 0.5]
    
print("Solução: ", independent_set)