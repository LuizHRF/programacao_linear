from extra import *

def guloso(grafo):

    out = grafo.copy()
    out.remove(out[0])

    n = len(grafo)
    
    c = []
    c.append(grafo[0])  ##Representa a melhor sequência encontrada até o momento

    while (len(c) < n):  ##Enquanto não tiverem todos os nodos em c

        v = c[-1].copy()
        
        nodo_proximo = 0
        menor_dist = distancia(v, out[0])

        for i in range(len(out)):

            dist = distancia(v, out[i])
            
            if dist < menor_dist:
                menor_dist = dist
                nodo_proximo = i
        
        c.append(out[nodo_proximo])
        out.remove(out[nodo_proximo])
        
    return c

##==================================================================================================
##PRINCIPAL
##==================================================================================================

caminho = "Trabalho1/instancias_caixeiro_viajante/"
arquivo = "2_inst2.tsp"
f = open(f'{caminho}{arquivo}', "r")

grafo, problema = ler_grafo(f)

melhor_caminho = guloso(grafo)

melhor_valor = custo_total(melhor_caminho)

print(f"Para o problema:")
problema.print()
print("A melhor solução encontrada foi: ", melhor_valor)