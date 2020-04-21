#Hello Moretto
# Import o pacote csv
import csv

class Grafo:
 
    def __init__(self, Nodes): #construtor
        self.nodes = Nodes
        self.adj_list = {}
        
        for node in self.nodes:
            self.adj_list[node] = []

    def add_edge(self, u, v): #Adiciona aresta
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def print_adj_list (self): #printa relação entre nós
        for node in self.nodes:
            print (node, '->', self.adj_list[node])

    #printa qtd de nós do grafo
    def quantidadeNos(self): 
        quantidade = []
        for node in self.nodes:
            quantidade.append(len(self.adj_list[node]))
        return quantidade