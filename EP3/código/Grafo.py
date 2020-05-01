#Hello Moretto para o EP3
# Import o pacote csv
import csv
from collections import defaultdict

class Grafo:
    def __init__(self, Nodes, V): #construtor
        self.V = V 
        self.nodes = Nodes
        self.adj = defaultdict(list)
        for node in self.nodes:
            self.adj[node] = []

    def add_edge(self, u, v): #Adiciona aresta
        self.adj[u].append(v)
        self.adj[v].append(u)

    def print_adj_list (self): #printa relação entre nós
        for node in self.nodes:
            print (node, '->', self.adj[node])

    #printa qtd de nós do grafo
    def quantidadeNos(self): 
        quantidade = []
        for node in self.nodes:
            quantidade.append(len(self.adj[node]))
        return quantidade

    def DFSUtil(self, temp, v, visited): 
  
        # Marca o vértice como visitado
        visited[v] = True
  
        # Store the vertex to list 
        # Salva o vértice na lista
        temp.append(v) 
  
        # Repeat for all vertices adjacent 
        # to this vertex v 
        for i in self.adj[v]:             
            if visited[i] == False: 
                  
                # Update the list 
                temp = self.DFSUtil(temp, i, visited) 
        return temp 

    # in an undirected graph 
    def connectedComponents(self): 
        visited = [] 
        cc = [] 
        for i in range(self.V): 
            visited.append(False) 
        for v in range(self.V): 
            if visited[v] == False: 
                temp = [] 
                cc.append(self.DFSUtil(temp, v, visited)) 
        return cc 
        