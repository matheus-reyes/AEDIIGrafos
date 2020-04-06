# Definindo a classe Local
class Local:

    # função construtor, que inicializa um Local com seus dados
    def __init__(self, coordenada_x, coordenada_y):
        self.coordenada_x = coordenada_x
        self.coordenada_y = coordenada_y
        self.frequentadores = []
        self.contador_frequentadores = 0
        self.prox = None

    # função adicionarFrequentador, que adiciona uma pessoa a lista de frequentadores de um local
    def adicionarFrequentador(self, id_pessoa):
        for pessoas in self.frequentadores:
            if pessoas == id_pessoa:
                return
        self.frequentadores.append(id_pessoa)
        self.contador_frequentadores += 1

    # função imprimirLocais, que imprime os Locais que já estão na lista
    def exportarLocais(self):
        return self.coordenada_x, self.coordenada_y, self.contador_frequentadores

    def imprimirLocaisComPrint(self):
        print("X: ", (self.coordenada_x))
        print("Y: ", (self.coordenada_y))
        print("N Pes: ", (self.contador_frequentadores))
