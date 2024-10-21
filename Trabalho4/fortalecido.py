# =======================================================
# Trabalho 4 - Programação Linear
# Alunos: Luiz Faccio e Robert Drey
# =======================================================
# Este script executa, para uma instância do problema do 
# conjunto independente máximo, a solução para o modelo 
# matemático fortalecido - com restrições extras.
# =======================================================

from t4_aux import *
from pyscipopt  import Model, quicksum

nome = "4_keller4"
grafo = le_grafo(f'Trabalho4/instancias_conjunto_independente_maximo/{nome}.clq')

modelo = Model("Conjunto Independente Maximo")

modelo.setParam("presolving/maxrounds", 0)
modelo.setParam("separating/maxrounds", 0)

vars = [modelo.addVar(name=str(v), vtype="B") for v in range(1, grafo.vertices + 1)]

modelo.setObjective(quicksum(vars), sense="maximize")

cons = {}
for i in range(1, grafo.getVertices()):
    for v in grafo.adjacencia[i]:
        cons[i] = modelo.addCons(vars[v] + vars[i] <= 1)

cliques = []
for i in range (1, grafo.getVertices()):
    clique = GeraClique(grafo, i)
    if len(clique) >2:
        cliques.append(clique)

for clique in cliques:
    a = [vars[v] for v in clique]
    print(a)
    modelo.addCons(quicksum(a) <= 1)

# print(modelo.getConss())

modelo.optimize()

independet_set  = [v for v in range(1, grafo.getVertices()) if modelo.getVal(vars[v]) == 1]

print(len(independet_set))