# Importa a classe Grafo do documento Grafo.py
from Grafo import Grafo

# Import o pacote csv
import csv

# Importa o módulo time que contém métodos para calcular tempo
import time

# Importa o módulo pickle para auxiliar a exportação
import pickle

print ("Começou!")
#inicia a contagem de tempo de execução
ini = time.time()

# Abre o arquivo e o lê com 'read' depois armazena em entrada_txt Encontros
entrada_txt = open('EP5/dados/traducao3.txt', 'r')

# Pula as primeiras linhas da entrada referentes ao: número de vértices e arestas | nome da coluna 
next(entrada_txt)
next(entrada_txt)

# Cria as listas para os vértices e arestas
nodes = []
all_edges = []

nos = 0

while nos < 5181:
    nodes.append(str(nos))
    nos += 1

# For que percorre a variável linha que contém as arestas e atribui a all_edges
for linha in entrada_txt:
    stripped_line = linha.strip()
    line_list = stripped_line.split()
    all_edges.append(line_list)

# Converte para slista de tuplas
all_edges = [tuple(l) for l in all_edges]

# Inicializa o construtor da classe Grafo e armazena na variável grafo
grafo = Grafo(len(nodes))

# Cria as arestas
for u,v in all_edges:
    grafo.add_edge(int(u),int(v))

# Fecha o documento
entrada_txt.close()

# Inicia a análise dos vértices
grafo.SIR()

# Exibe o número de passos com os dados da situação da pessoa
saida_passos = (grafo.saida_passos)

# Escreve no arquivo de saída a lista de listas do SIR
# with open('EP5/dados/saida_09_02.pkl', 'wb') as f:
#     pickle.dump(saida_passos, f)
# f.close()

# # Apenas para ler o arquivo de saída
with open('EP5/dados/saida_06_05.pkl', 'rb') as fb:
    mynewlist = pickle.load(fb)
print(mynewlist)

# Calcula o tempo de execução ao final do processamento
fim = time.time()
# Fim do Processamento
print ("Acabou!")
# Exibe na tela o tempo de processamento do código
print("Tempo de execuçao (S): ", fim-ini)