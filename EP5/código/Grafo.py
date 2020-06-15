import random

class Grafo:

    # Construtor que recebe o número de vértices e inicia o vetor de adjacentes
    def __init__(self, V):
        self.V = V 
        self.adj = [[] for i in range(V)] 
        self.estado = ['S' for i in range(V)]
        pacienteZero = random.randint(0, V)
        self.estado[pacienteZero] = 'I'
        self.c = 0.9
        self.r = 0.2
        self.passos = 0
        self.saida_passos = []

    def step_count(self):
        saida = [0,0,0]  # [S, I, R]
        for i in self.estado:
            if i == 'S':
                saida[0] += 1
            elif i == 'I':
                saida[1] += 1
            else:
                saida[2] += 1
        self.saida_passos.append(saida)

    # Função que recebe dois vértices e cria uma aresta entre eles, adicionando-os em seus vértices de adjacentes
    def add_edge(self, u, v): 
        self.adj[u].append(v)
        self.adj[v].append(u)

    # Função que exibe na tela cada vértice e sua lista de adjacência
    def print_adj_list (self): 
        for node in self.nodes:
            print(node, '->', self.adj[node])

    # Função que exibe na tela a quantidade de vértices em cada lista de adjacência
    def quantidadeNos(self): 
        quantidade = []
        for node in self.nodes:
            quantidade.append(len(self.adj[node]))
        return quantidade

    # Função que realiza a Depth-first search
    def DFSUtil(self, temp, v, visited): 
        self.step_count()
        # Marca o vértice passado como visitado
        visited[v] = True

        x = random.uniform(0, 1)

        # Se x for menor ou igual a probabilidade de recuperação
        if x <= self.r:
            self.estado[v] = 'R'
            self.DFSUtil(temp, (v + 1), visited)

        y = random.uniform(0, 1)

        # Se y for menor ou igual a probabilidade de contágio
        if y <= self.c and self.estado[v] != 'R':
            self.estado[v] = 'I'

        # Salva o vértice na lista
        temp.append(v) 
      
        #gv (Guarda Visitados): Guarda o caminho feito
        gv = []
        gv.append(v)

        # Repete o processo para todos os vértices adjacentes
        while (len(gv) != 0):
            for i in self.adj[gv[len(gv)-1]]:             
                if visited[i] == False:
                    gv.append(i)
                    visited[i] = True
                    temp.append(i)
            del(gv[len(gv)-1])
        
        return temp

    # Função que Atualiza os componentes conexos do grafo
    def SIR(self): 
        # Vetor de vértices visitados e de componentes conexos respectivamente
        visited = [] 

        # Inicializa o vetor de visitados com todos os valores igual a false
        for i in range(self.V): 
            visited.append(False) 

        # Para cada vértice não visitado, chama a função de Depth-first search
        for v in range(self.V): 
            if visited[v] == False: 
                temp = [] 
                self.DFSUtil(temp, v, visited)