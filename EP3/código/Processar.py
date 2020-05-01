# Hello Moretto
# Importa a classe Grafo do documento Grafo.py
from Grafo import Grafo
print ("Começo")

# Import o pacote csv
import csv

# Importa o módulo time que contém métodos para calcular tempo
import time

print ("Começou!")
#inicia a contagem de tempo de execução
ini = time.time()

# Abre o arquivo Planilha_teste.csv e o lê com 'read' depois armazena em entrada_csv
entrada_csv = open('EP3/dados/Planilha_teste.csv', 'r')
# Abre o arquivo teste.txt e o lê com 'read' depois armazena em entrada_txt
entrada_txt = open('EP3/dados/teste.txt', 'r')

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

# Printa as arestas  
# print(all_edges)

# Inicializa o construtor da classe Grafo e armazena na variável grafo
grafo = Grafo(nodes, len(nodes))

# Cria as arestas
for u,v in all_edges:
    grafo.add_edge(u,v)

#printa os nós com suas devidas conexões
grafo.print_adj_list()

# Fecha o documento
entrada_csv.close()
entrada_txt.close()

cc = grafo.connectedComponents() 
print("Following are connected components") 
print(cc) 

# # Escreve no arquivo de saída os graus dos nós linha por linha
# with open('EP3/dados/Tabela_Saida.csv', 'w', newline='') as fp:
#     a = csv.writer(fp, delimiter =',')
#     a.writerows(map(lambda x: [x], cc))


import csv

with open("out.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(cc)


# nodes = [0, 1, 2, 3, 4, 5]

# g = Grafo(nodes, len(nodes)); 

# g.add_edge(1, 0) 
# g.add_edge(2, 3) 
# g.add_edge(3, 4) 


# Calcula o tempo de execução ao final do processamento

# Fim do Processamento
print ("Acabou!")

# Exibe na tela o tempo de processamento do código
print("Tempo de execuçao (S): ", fim-ini)