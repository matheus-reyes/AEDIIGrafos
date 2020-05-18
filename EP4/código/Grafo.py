
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

    #printa quantdade de nós do grafo
    def quantidadeNos(self): 
        quantidade = []
        for node in self.nodes:
            quantidade.append(len(self.adj_list[node]))
        return quantidade

    # Função que encontra o menor caminho entre dois nós
    def bfs_shortest_path(self, graph, start, goal):
        # guarda o caminho dos nós explorados
        explored = []
        # guarda o todos os caminhos a serem checados
        queue = [[start]]

        # Caso os vértices sejam iguais
        if start == goal:
            return 0

        # mantem o loop até checar todas as possibilidades
        while queue:
            path = queue.pop(0)
            # pega o ultimo nó
            node = path[-1]
            if node not in explored:
                neighbours = graph[node]
                # vai visitar todos os caminhos possiveis pelos vizinhos
                for neighbour in neighbours:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)
                    # retorna o caminho se o vizinho é o objetivo
                    if neighbour == goal:
                        return len(new_path) - 1

                # marca o nó já visitado
                explored.append(node)

        # caso não haja nenhum caminho entre os nós
        return 0