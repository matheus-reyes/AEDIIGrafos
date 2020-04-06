# Importa a classe Local do documento Local.py
from Local import Local
# Importa o módulo csv que contém métodos para ler e escrever dados csv
import csv

# Variáveis Globais
inicio = None
quantidade = 0

# Função inserirLocal, que insere um Local na lista
def inserirLocal(id_pessoa, coordenada_x, coordenada_y):
    if coordenada_x == 0 and coordenada_y == 0:
        return
    else:
        global quantidade
        global inicio
        # Caso já tenham Locais na lista
        if inicio:
            ponteiro = inicio
            # Enquanto o elemento tiver próximo na lista
            while(ponteiro.prox):
                # Caso já tenham locais iguais na lista, é adicionado idpessoa no vetor frequentadores e a função é retornada
                if ponteiro.coordenada_x == coordenada_x and ponteiro.coordenada_y == coordenada_y:
                    ponteiro.adicionarFrequentador(id_pessoa)
                    return
                ponteiro = ponteiro.prox
            # Caso não tenham Locais iguais e não tenham mais próximos na lista, adiciona o novo local e ajusta o ponteiro prox anterior
            Local(coordenada_x, coordenada_y)
            ponteiro.prox = Local(coordenada_x, coordenada_y)
            ponteiro.prox.adicionarFrequentador(id_pessoa)
        # Caso ainda não tenham Locais na lista
        else:
            Local(coordenada_x, coordenada_y)
            inicio = Local(coordenada_x, coordenada_y)
            inicio.adicionarFrequentador(id_pessoa)
        quantidade = quantidade + 1

# Função exibirLocais, que exibe os locais que já estão na lista
def exibirLocais():
    global quantidade
    global inicio
    ponteiro = inicio
    contador = 0
    while(contador < quantidade):
        ponteiro.imprimirLocaisComPrint()
        ponteiro = ponteiro.prox
        contador = contador + 1

# Função escrever_csv, escreve todas as informções de coordenadas e quantidade de pessoas
def escrever_csv():
    global quantidade
    global inicio

    # Tivemos que usar newline="" para evitar adicionar linhas desnecessárias
    with open ('dados/Tabela_Saida.csv', 'w', newline='') as saida_csv:
        writer = csv.writer(saida_csv)
        writer.writerow( ('X', 'Y', 'numero_pessoas') )
        ponteiro = inicio
        contador = 0
        while(contador < quantidade):
            linha = ponteiro.exportarLocais()
            writer.writerow(linha)
            ponteiro = ponteiro.prox
            contador = contador + 1
        saida_csv.close()    

# Função quantidadeLocais, que exibe o número de locais que estão na lista
def quantidadeLocais():
    global quantidade
    print("Quantidade de Locais: %d" % (quantidade))