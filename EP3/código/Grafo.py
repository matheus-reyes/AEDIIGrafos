
class Grafo:

    # Construtor que recebe o número de vértices e inicia o vetor de adjacentes
    def __init__(self, V):
        self.V = V 
        self.adj = [[] for i in range(V)] 

    # Função que recebe dois vértices e cria uma aresta entre eles, adicionando-os em seus vértices de adjacentes
    def add_edge(self, u, v): 
        self.adj[u].append(v)
        self.adj[v].append(u)

    # Função que exibe na tela cada vértice e sua lista de adjacência
    def print_adj_list (self): 
        for node in self.nodes:
            print (node, '->', self.adj[node])

    # Função que exibe na tela a quantidade de vértices em cada lista de adjacência
    def quantidadeNos(self): 
        quantidade = []
        for node in self.nodes:
            quantidade.append(len(self.adj[node]))
        return quantidade

    # Função que realiza a Depth-first search
    def DFSUtil(self, temp, v, visited): 
  
        # Marca o vértice passado como visitado
        visited[v] = True
  
        # Salva o vértice na lista
        temp.append(v) 
      
        #gv (Guarda Visitados): Guarda o caminho feito
        gv = []
        gv.append(v)

        # Repeat for all vertices adjacent 
        # to this vertex v 
        while (len(gv) != 0):
            for i in self.adj[gv[len(gv)-1]]:             
                if visited[i] == False:
                    # Update the list 
                    gv.append(i)
                    visited[i] = True
                    temp.append(i)
                    #temp = self.DFSUtil(temp, i, visited) 
            del(gv[len(gv)-1])
        
        return temp


  
       

        

    # Função que Atualiza os componentes conexos do grafo
    def connectedComponents(self): 
        # Vetor de vértices visitados e de componentes conexos respectivamente
        visited = [] 
        cc = []

        # Inicializa o vetor de visitados com todos os valores igual a false
        for i in range(self.V): 
            visited.append(False) 

        # Para cada vértice não visitado, chama a função de Depth-first search
        for v in range(self.V): 
            if visited[v] == False: 
                temp = [] 
                cc.append(self.DFSUtil(temp, v, visited)) 
        return cc 