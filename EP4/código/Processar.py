# Importa a classe Grafo do documento Grafo.py
from Grafo import Grafo

# Import o pacote csv
import csv

# Importa o módulo time que contém métodos para calcular tempo
import time

print ("Começou!")
ini = time.time()

# Abre o arquivo e o lê c
#inicia a contagem de tempo de execuçãoom 'read' depois armazena em entrada_csv Ids_Pessoas
entrada_csv = open('EP4/dados/planilha_teste.csv', 'r')
# Abre o arquivo e o lê com 'read' depois armazena em entrada_txt Encontros
entrada_txt = open('EP4/dados/teste.txt', 'r')

# Pula as primeiras linhas da entrada referentes ao: número de vértices e arestas | nome da coluna 
next(entrada_txt)   
next(entrada_txt)
next(entrada_csv)

# Lê a variável entrada com o método reader e a armazena na variável dados
dados_tabela = csv.reader(entrada_csv)

# Cria as listas para os vértices e arestas
nodes = []
all_edges = []

# For que percorre a variável dados que contém todos os dados da tabela CSV
for dados in dados_tabela:
    nodes.append(dados[0])

# For que percorre a variável linha que contém as arestas e atribui a all_edges
for linha in entrada_txt:
    stripped_line = linha.strip()
    line_list = stripped_line.split()
    all_edges.append(line_list)

# Converte para lista de tuplas
all_edges = [tuple(l) for l in all_edges]

# Inicializa o construtor da classe Grafo e armazena na variável grafo
grafo = Grafo(nodes)

# Cria as arestas
for u,v in all_edges:
    grafo.add_edge(u,v)

# listas de adjacências
adj_list = grafo.print_adj_list()

adjacentes = {}

for elemento in adj_list:
    adjacentes[elemento[0]] = elemento[1:]

print(grafo.bfs_shortest_path(adjacentes, '1', '2'))  # returna o menor caminho