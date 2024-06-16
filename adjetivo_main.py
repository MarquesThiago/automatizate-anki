# -*- coding: utf-8 -*-

import pandas as pd

# Substitua 'nome_do_arquivo.xlsx' pelo nome do seu arquivo Excel
# Substitua 'nome_da_planilha' pelo nome da planilha dentro do arquivo Excel
# Substitua 'coluna1', 'coluna2' e 'coluna3' pelos nomes das colunas que você
nome_do_arquivo = r'excels\adjetivos_corrigido.xlsx'
nome_da_planilha = 'lista-adjetivos'
colunas = ['coluna1', 'coluna2', 'coluna3']

# Lendo o arquivo Excel
dados = pd.read_excel(
    nome_do_arquivo
)
print(dados.head())

# Lendo as colunas específicas
# coluna1 = dados['coluna1'].tolist()
# coluna2 = dados['coluna2'].tolist()
# coluna3 = dados['coluna3'].tolist()

# Exibindo as primeiras linhas das listas
# print("Lista da Coluna 1:")
# print(coluna1[:5])  # Exibe as primeiras 5 linhas da lista
# print("\nLista da Coluna 2:")
# print(coluna2[:5])  # Exibe as primeiras 5 linhas da lista
# print("\nLista da Coluna 3:")
# print(coluna3[:5])  # Exibe as primeiras 5 linhas da lista
