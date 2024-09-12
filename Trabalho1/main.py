from guloso import *
from bruto import *
import os
import time
from concurrent.futures import ThreadPoolExecutor, TimeoutError

caminho = "Trabalho1/instancias_caixeiro_viajante/"
# caminho = "Trabalho1/teste/"

resultados = []
tempo_limite = 60  ##Segundos

def executar_algoritmo_bruto(grafo):
    return bruto(grafo)

def executar_algoritmo_guloso(grafo):
    melhor_caminho = guloso(grafo)
    return custo_total(melhor_caminho)

for nome in os.listdir(caminho):
    caminho_completo = os.path.join(caminho, nome)
    
    if os.path.isfile(caminho_completo):
        print(f"Executando algoritmo no arquivo: {nome}")
        
        with open(caminho_completo, 'r') as arquivo:
            grafo, problema = ler_grafo(arquivo)

            with ThreadPoolExecutor() as executor:
                try:
                    print("  Executando algoritmo bruto")
                    inicio_bruto = time.perf_counter()
                    futuro_bruto = executor.submit(executar_algoritmo_bruto, grafo)
                    custo_bruto = futuro_bruto.result(timeout=tempo_limite)
                    final_bruto = time.perf_counter()
                except TimeoutError:
                    print(f"  Algoritmo bruto excedeu o tempo limite de {tempo_limite /60} minutos no arquivo {nome}.")
                    custo_bruto = None
                    final_bruto = inicio_bruto 

                try:
                    print("  Executando algoritmo guloso")
                    inicio_guloso = time.perf_counter()
                    futuro_guloso = executor.submit(executar_algoritmo_guloso, grafo)
                    custo_guloso = futuro_guloso.result(timeout=tempo_limite)
                    final_guloso = time.perf_counter()
                except TimeoutError:
                    print(f"  Algoritmo guloso excedeu o tempo limite de {tempo_limite / 60} minutos no arquivo {nome}.")
                    custo_guloso = None
                    final_guloso = inicio_guloso 

            resultado = {
                "arquivo": nome,
                "custo_bruto": custo_bruto,
                "custo_guloso": custo_guloso,
                "tempo_bruto": final_bruto - inicio_bruto,
                "tempo_guloso": final_guloso - inicio_guloso,
            }

            resultados.append(resultado)

            print(f"  Nome do arquivo: {resultado['arquivo']}")
            print(f"  Custo Bruto: {resultado['custo_bruto']}")
            print(f"  Custo Guloso: {resultado['custo_guloso']}")
            print(f"  Tempo Bruto: {resultado['tempo_bruto']} segundos")
            print(f"  Tempo Guloso: {resultado['tempo_guloso']} segundos")
