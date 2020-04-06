# Importa o documento ListaLigada.py
import ListaLigada
# Importa a classe Local do documento ListaLigada.py
from Local import Local
# Importa o módulo csv que contém métodos para ler e escrever dados csv
import csv
# Importa o módulo time que contém métodos para calcular tempo
import time

print("Começou!")
#inicia a contagem de tempo de execução
ini = time.time()

# Abre o arquivo tabela-teste.csv e o lê com 'read' depois armazena em entrada
entrada_csv = open('dados/Tabela_Teste.csv', 'r')

# lê a variável entrada com o método reader e a armazena na variável dados
dados_tabela = csv.reader(entrada_csv)

# Ignora a primeira linha, que contêm os nomes das colunas
next(dados_tabela)

# Número da coluna que contém os ids das pessoas
coluna_id_pessoa = 0
# Número da coluna que contém as coordenadas x e y de domicílio
coluna_CO_DOM_x = 1
coluna_CO_DOM_y = 2
# Número da coluna que contém as coordenadas x e y de escola
coluna_CO_ESC_x = 4
coluna_CO_ESC_y = 5
# Número da coluna que contém as coordenadas x e y de trabalho_1
coluna_CO_TR1_x = 7
coluna_CO_TR1_y = 8
# Número da coluna que contém as coordenadas x e y de trabalho_2
coluna_CO_TR2_x = 10
coluna_CO_TR2_y = 11
# Número da coluna que contém as coordenadas x e y de origem
coluna_CO_O_x = 13
coluna_CO_O_y = 14
# Número da coluna que contém as coordenadas x e y de destino
coluna_CO_D_x = 17
coluna_CO_D_y = 18
# Número da coluna que contém as coordenadas x e y de primeira transferência
coluna_CO_T1_x = 20
coluna_CO_T1_y = 21
# Número da coluna que contém as coordenadas x e y de segunda transferência
coluna_CO_T2_x = 23
coluna_CO_T2_y = 24
# Número da coluna que contém as coordenadas x e y de terceira transferência
coluna_CO_T3_x = 26
coluna_CO_T3_y = 27

# For que percorre a variável dados que contém todos os dados da tabela CSV
for dados in dados_tabela:
    # Insere os locais na lista, passando a Coordenada X, Coordenada Y e IDPessoa de cada objeto
    ListaLigada.inserirLocal(int(dados[coluna_id_pessoa]), int(dados[coluna_CO_DOM_x]), int(dados[coluna_CO_DOM_y]))
    ListaLigada.inserirLocal(int(dados[coluna_id_pessoa]), int(dados[coluna_CO_ESC_x]), int(dados[coluna_CO_ESC_y]))
    ListaLigada.inserirLocal(int(dados[coluna_id_pessoa]), int(dados[coluna_CO_TR1_x]), int(dados[coluna_CO_TR1_y]))
    ListaLigada.inserirLocal(int(dados[coluna_id_pessoa]), int(dados[coluna_CO_TR2_x]), int(dados[coluna_CO_TR2_y]))
    ListaLigada.inserirLocal(int(dados[coluna_id_pessoa]), int(dados[coluna_CO_O_x]), int(dados[coluna_CO_O_y]))
    ListaLigada.inserirLocal(int(dados[coluna_id_pessoa]), int(dados[coluna_CO_D_x]), int(dados[coluna_CO_D_y]))
    ListaLigada.inserirLocal(int(dados[coluna_id_pessoa]), int(dados[coluna_CO_T1_x]), int(dados[coluna_CO_T1_y]))
    ListaLigada.inserirLocal(int(dados[coluna_id_pessoa]), int(dados[coluna_CO_T2_x]), int(dados[coluna_CO_T2_y]))
    ListaLigada.inserirLocal(int(dados[coluna_id_pessoa]), int(dados[coluna_CO_T3_x]), int(dados[coluna_CO_T3_y]))

# Printa os locais no terminal
ListaLigada.exibirLocais()

# Exporta os locais em um documento csv separado por linhas
ListaLigada.escrever_csv()

# Exibe a quantidade de Locais
print("quantidade de locais: %d" % ListaLigada.quantidade)

# Fecha o documento
entrada_csv.close()

# Calcula o tempo de execução ao final do processamento
fim = time.time()

print("Acabou!")

# Exibe na tela o tempo de processamento do código
print("Tempo de execuçao (S): ", fim-ini)