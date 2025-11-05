import pandas as pd

# Criando um DataFrame

data = {
    'Nome':     ['Caio', 'Vicente', 'Davi', 'Fabiano', 'Marlon','Claudio'],
    'Idade':    [25,30,35,40,45,60],
    'Salario':  [5000,6000,7000,8000,9000,10000]


}

df = pd.DataFrame(data)

# Exibindo o dataframe
print('Dataframe')
print(df)

# Selecionando uma coluna
print("\n Coluna nome:")
print(df['Nome'])

# Filtrando dados
print("\n Pessoas com idade maior que 30 anos")
print( df[df['Idade'] > 30] )

# Adicionando uma nova coluna de imposto
df['Imposto'] = df['Salario'] * 0.12
print('\n Nova Coluna de Imposto:')
print(df)

# Calculando a media salarial
media_salarial = df['Salario'].mean()
print('\nMédia do salario: ')
print(media_salarial)

# Calculos simples comuns:

print('\n Menor salario:')
print(df['Salario'].min())

print('\n Maior salario:')
print(df['Salario'].max())  

print('\n Soma dos salarios:')
print(df['Salario'].sum())

# Estatisticas gerais dos dados
print(df.describe())

# Ordenar por salario
print("\n Ordenado por Salario: ")
print(df.sort_values(by='Salario', ascending=False))

# Desafio: Criar uma coluna de setor
df['Setor'] = ['TI', 'RH', 'TI', 'RH', 'Financeiro', 'Financeiro']
print('\nAdicionando o setor:')
print(df)

# Agrupar por setor

print('\n Media Salarial por Setor: ')
print(df.groupby('Setor')['Salario'].mean())

# Contar por setor
print('\n Quantidade por setor')
print(df['Setor'].value_counts())

# Criando um dataframe bonus
bonus_data = {
    'Nome':['Caio', 'Vicente', 'Davi', 'Fabiano', 'Marlon','Claudio'],
    'Bonus':[500, 600, 700, 800, 900, 1000]
    }

df_bonus = pd.DataFrame(bonus_data)
# Realizando o merge dos dois dataframes
df_merged = pd.merge(df, df_bonus, on='Nome')

print('Dataframe final com o bonus:')
print(df_merged)

# Criar uma coluna de salario final (Salario - Imposto + Bonus
df_merged['Salario_Final'] = df_merged['Salario'] - df['Imposto'] + df_merged['Bonus']

# Salario final
print("Dataframe com salario final:")
print(df_merged)

# Salvar em CSV
# o comando r, faz com que não precise utilizar o comando / para as pastas
df.to_csv(r'C:\Users\vicente.bacelar\Desktop\Python_EAD\salarios.csv', index=False)
print('\n Arquivo gerado com sucesso! ')
