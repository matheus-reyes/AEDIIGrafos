# Importa o documento ListaLigada.py
import ListaLigada
# Importa a classe Local do documento ListaLigada.py
from Local import Local
# Importa o módulo csv que contém métodos para ler e escrever dados csv
import csv
# Abre o arquivo tabela-teste.csv e o lê com 'read' depois armazena em entrada
entrada_csv = open('Tabela_Virgulas.csv', 'r')
# lê a variável entrada com o método reader e a armazena na variável dados
dados_tabela = csv.reader(entrada_csv)
# Ignora a primeira linha, que contêm os nomes das colunas
next(dados_tabela)
# Número da coluna que contém os ids das pessoas
coluna_id_pessoa = 43
# Número da coluna que contém as coordenadas x de destino
coluna_coordenada_x = 88
# Número da coluna que contém as coordenadas y de destino
coluna_coordenada_y = 89

# For que percorre a variável dados que contém todos os dados da tabela CSV
for dados in dados_tabela:
    # Insere os locais na lista, passando a Coordenada X, Coordenada Y e IDPessoa de cada objeto
    ListaLigada.inserirLocal(int(dados[coluna_coordenada_x]), int(dados[coluna_coordenada_y]), int(dados[coluna_id_pessoa]))

# Printa os locais no terminal
ListaLigada.exibirLocais()
# Exporta os locais em um documento csv separado por linhas
ListaLigada.escrever_csv()
# Exibe a quantidade de Locais
print("quantidade de locais: %d" % ListaLigada.quantidade)

# Fecha o documento
entrada_csv.close()