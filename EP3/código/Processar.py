# Importa a classe Grafo do documento Grafo.py
from Grafo import Grafo

# Import o pacote csv
import csv

print ("Começou!")

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
grafo = Grafo(len(nodes) + 1)

# Cria as arestas
for u,v in all_edges:
    grafo.add_edge(int(u),int(v))

# Fecha o documento
entrada_csv.close()
entrada_txt.close()

# Recebe os componentes conexos na variável cc
cc = grafo.connectedComponents()
# Deleta o primeiro componente, pois não existe pessoa com id 0, as pessoas começam com id 1
del cc[0]
# Exibe os componentes conexos
print("Componentes Conexos: ") 
print(cc) 

# # Escreve no arquivo de saída os graus dos nós linha por linha
# with open('EP3/dados/Tabela_Saida.csv', 'w', newline='') as fp:
#     a = csv.writer(fp, delimiter =',')
#     a.writerows(map(lambda x: [x], cc))


# with open("out.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerows(cc)


# nodes = [3, 4, 5]

# g = Graph(6); 

# g.addEdge(4, 5) 
# g.addEdge(3, 4) 

# cc = g.connectedComponents() 
# print("Following are connected components") 
# print(cc) 


# # Calcula o tempo de execução ao final do processamento

# # Fim do Processamento
# print ("Acabou!")
