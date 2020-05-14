
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
        lista = []
        contador = 0
        
        for node in self.nodes:
            lista.append(self.adj_list[node])
            lista[contador].insert(0, node)
            contador += 1
        return lista

    def adj_list (self):
        return self.adj_list

    #printa qtd de nós do grafo
    def quantidadeNos(self): 
        quantidade = []
        for node in self.nodes:
            quantidade.append(len(self.adj_list[node]))
        return quantidade

    # finds shortest path between 2 nodes of a graph using BFS
    def bfs_shortest_path(self, graph, start, goal):
        # keep track of explored nodes
        explored = []
        # keep track of all the paths to be checked
        queue = [[start]]

        # return path if start is goal
        if start == goal:
            return "That was easy! Start = goal"

        # keeps looping until all possible paths have been checked
        while queue:
            # pop the first path from the queue
            path = queue.pop(0)
            # get the last node from the path
            node = path[-1]
            if node not in explored:
                neighbours = graph[node]
                # go through all neighbour nodes, construct a new path and
                # push it into the queue
                for neighbour in neighbours:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)
                    # return path if neighbour is goal
                    if neighbour == goal:
                        return new_path

                # mark node as explored
                explored.append(node)

        # in case there's no path between the 2 nodes
        return "So sorry, but a connecting path doesn't exist :("