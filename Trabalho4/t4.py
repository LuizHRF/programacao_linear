from t4_aux import *
from pyscipopt import Model

grafo = le_grafo('Trabalho4/instancias_conjunto_independente_maximo/1_hamming6-2.clq')

modelo = Model("Conjunto Independente Maximo")

modelo.setParam("presolving/maxrounds", 0)
modelo.setParam("separating/maxrounds", 0)

vars = {}
for v in range(1, grafo.vertices + 1):
    vars[v] = modelo.addVar(name=str(v), vtype="BINARY", obj=1.0)

print(vars)