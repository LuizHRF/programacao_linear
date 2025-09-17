# Programação Linear e Otimização Combinatória

Este repositório contém implementações e soluções para problemas clássicos de otimização combinatória desenvolvidos durante a disciplina de Programação Linear. Os projetos abordam diferentes algoritmos e técnicas, desde abordagens heurísticas até modelos de programação linear inteira.

A **otimização combinatória** é o campo da matemática aplicada que busca encontrar a melhor solução dentro de um conjunto finito de possibilidades, onde as variáveis assumem valores discretos (inteiros ou binários). Estes problemas são frequentemente NP-difíceis, exigindo algoritmos especializados como programação linear inteira, heurísticas ou programação dinâmica. A **programação linear** modela problemas onde tanto a função objetivo quanto as restrições são lineares, permitindo o uso de algoritmos eficientes como Simplex, mas suas soluções podem ser fracionárias. Já a **programação linear inteira** estende esse conceito exigindo que algumas ou todas as variáveis sejam inteiras, sendo resolvida através de métodos como Branch-and-Bound.

A **programação dinâmica** é uma técnica que resolve problemas complexos dividindo-os em subproblemas menores, armazenando resultados para evitar recálculos, sendo ideal para problemas com subestrutura ótima. Os **algoritmos heurísticos** oferecem soluções aproximadas em tempo computacional aceitável, enquanto as **metaheurísticas** são estratégias de alto nível inspiradas na natureza (como algoritmos genéticos) para guiar a busca por melhores soluções. Estas técnicas têm ampla aplicação em logística, telecomunicações, finanças, bioinformática e planejamento, sendo implementadas através de ferramentas como PuLP, SCIP e Gurobi para resolver problemas como o Caixeiro Viajante, Problema da Mochila e Conjunto Independente Máximo.

## Estrutura

### Trabalho 1 - Problema do Caixeiro Viajante (TSP)

Implementação de dois algoritmos para resolver o Problema do Caixeiro Viajante:

#### Algoritmos Implementados
- **Força Bruta (`bruto.py`)**: Enumera todas as permutações possíveis para encontrar a solução ótima
- **Algoritmo Guloso (`guloso.py`)**: Heurística do vizinho mais próximo para soluções aproximadas

#### Características
- **Instâncias**: 12 instâncias de teste variando de pequeno a grande porte
- **Comparação de Performance**: Análise de tempo de execução e qualidade das soluções
- **Timeout**: Limite de 60 segundos para execução de cada algoritmo
- **Execução Paralela**: Uso de ThreadPoolExecutor para otimizar os testes

### Trabalho 2 - Problema dos Rótulos

Solução do problema de posicionamento de rótulos usando Programação Linear Inteira.

#### Descrição do Problema
- **Objetivo**: Maximizar o número de rótulos não sobrepostos em um mapa
- **Restrições**: Rótulos não podem se sobrepor
- **Modelagem**: Problema de programação linear inteira binária

#### Implementação
- **Biblioteca**: PuLP para modelagem em Python
- **Variáveis**: Binárias indicando se um rótulo é selecionado
- **Função Objetivo**: Maximizar a soma das variáveis binárias
- **Restrições**: Para cada par de rótulos que se sobrepõem: x_i + x_j ≤ 1

### Trabalho 4 - Conjunto Independente Máximo

Implementação de diferentes formulações para o problema do Conjunto Independente Máximo em grafos.

#### Modelos Implementados
1. **Modelo Básico (`basico.py`)**
   - Formulação padrão com restrições de adjacência
   - Variáveis binárias para cada vértice
   - Restrição: x_u + x_v ≤ 1 para cada aresta (u,v)

2. **Modelo Fortalecido 1 (`fortalecido_1.py`)**
   - Modelo básico + restrições de clique
   - Identifica a maior clique e adiciona restrição de cardinalidade
   - Melhora a relaxação linear

3. **Modelo Fortalecido 2 (`fortalecido_2.py`)**
   - Extensão com múltiplas restrições de fortalecimento
   - Análise mais detalhada das estruturas do grafo

#### Características
- **Solver**: PySCIPOpt para otimização
- **Instâncias**: 8 instâncias de grafos de diferentes tipos e tamanhos
- **Análise Comparativa**: Jupyter notebook para visualização dos resultados
- **Valores Ótimos**: Arquivo com soluções conhecidas para validação

##  Tecnologias Utilizadas

- **Python 3.12**: Linguagem principal
- **PuLP**: Modelagem de programação linear (Trabalho 2)
- **PySCIPOpt**: Solver de otimização (Trabalho 4)
- **Jupyter Notebook**: Análise e visualização
- **Concurrent.futures**: Execução paralela e controle de timeout

## Tipos de Problemas Abordados

1. **TSP (Travelling Salesman Problem)**: Problema de otimização em grafos
2. **Problema dos Rótulos**: Otimização geométrica e espacial  
3. **Conjunto Independente Máximo**: Teoria dos grafos e cliques
4. **Problema da Mochila**: Programação dinâmica e otimização combinatória

## 👥 Autores

- **Luiz Faccio**
- **Robert Drey**

---

Este repositório demonstra a aplicação prática de conceitos fundamentais em otimização combinatória, desde implementações algorítmicas básicas até o uso de ferramentas profissionais de modelagem matemática, em um ambiente de aprendizagem.