# ==========================================================
# Analise simples com Numpy + Pandas
# Dataset: drinks.csv da fivethirtyeight
# ==========================================================

import numpy as np
import pandas as pd

# 1) Ler o Arquivo CSV
df = pd.read_csv(r'C:\Users\vicente.bacelar\Desktop\Python_EAD\drinks.csv')

print("Primeiras Linhas do dataset: ")
print(df.head())

# 2) Selecionar as colunas de bebidas
colunas_bebidas = ['beer_servings','spirit_servings', 'wine_servings']

# Verificar se todas existem antes de usar
print('\nColunas encontradas no arquivo: ')
print(df.columns)

# 3) Calcular Soma das bebidas por pais
# print(df['beer_servings'].values)

# Convertendo para a Array
dados_bebidas = df[colunas_bebidas].values
# Somando linha a linha
df['total_bebidas'] = np.sum(dados_bebidas, axis=1)

print('\nTotal de bebidas por pais: ')
print(df[['country', 'total_bebidas']].head())

# 4) Calcular a média total global

media_global = np.mean(df['total_bebidas'].values)
print('\nMedia global de consumo: ')
print(media_global)

# 5) Criar coluna marcando quem está acima ou abaixo da média // head  vai mostrar somente alguns itens

df['acima_media'] = np.where(df['total_bebidas'] > media_global, 'Sim', 'Nao')
print ('\nPaises acima da media: ')
print (df[['country', 'total_bebidas', 'acima_media']].head())

# 6) Contar paises acima e abaixo da media

qtd_acima = (df['acima_media'] == 'Sim').sum()                           
qtd_abaixo = (df['acima_media'] == 'Nao').sum()

print('\nQuantidade de paises acima da media: ', qtd_acima)
print('\nQuantidade de paises abaixo da media: ', qtd_abaixo)

# 7) Mostrar apenas paises acima da media
paises_acima = df[df['acima_media'] == 'Sim']
print('\nPaises acima da media de consumo: ')
print(paises_acima[['country', 'total_bebidas']].sort_values(by='total_bebidas',ascending=False))

# 8) Paises que mais bebem, cerveja:
top_cerveja = df.sort_values(by='beer_servings', ascending=False)
print('\nTop 10 paises que mais consomem cerveja: ')
print(top_cerveja[['country','beer_servings']].head(10))

# 9) Salvar Resultado final
df.to_csv(r'C:\Users\vicente.bacelar\Desktop\Python_EAD\resultado_analise.csv', index=False)
print('\nArquivo "resultado_analise_drinks.csv" salvo com sucesso!')
