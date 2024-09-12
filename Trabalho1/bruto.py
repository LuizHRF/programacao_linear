from extra import *
import itertools
import time

def bruto(grafo):
    n = len(grafo)

    permutacoes = itertools.permutations(grafo)

    melhor_custo = float('inf')
    for p in permutacoes:
        custo = custo_total(p)
        if (custo < melhor_custo):
            melhor_custo = custo
    
    return melhor_custo

##==================================================================================================
##PRINCIPAL
##==================================================================================================


caminho = "Trabalho1/instancias_caixeiro_viajante/"
arquivo = "1_inst1.tsp"
f = open(f'{caminho}{arquivo}', "r")

grafo, problema = ler_grafo(f)

inicio = time.time()
melhor_custo = bruto(grafo)
fim = time.time()

tempo_execucao = fim - inicio

print(f"Para o problema:")
problema.print()
print("A melhor solução encontrada foi: ", melhor_custo)
print("Tempo de execução: ", tempo_execucao)
