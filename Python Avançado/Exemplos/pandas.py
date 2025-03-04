import pandas as pd
import sqlite3 as sql

df_cardio = pd.read_json('Cardio json')
print(df_cardio)

print(type(df_cardio))

print(type(df_cardio['calories']))

print(type(df_cardio.index))

#Mostrar as primeiras 5 linhas
print(df_cardio.head())

#Para Mostrar as ultimas 5 linhas
print(df_cardio.tail())

#Remover uma Coluna
df_cardio.drop(colums=['Maxpulse'])

print(df_cardio * 3)
print(df_cardio / 2)
print(df_cardio + df_cardio)

print(df_cardio.describe())

print(df_cardio.info())

#Tratando valores não nulos

df_cardio['Calories'] = df_cardio['Calories'].fillna(0)
df_cardio['Calories'] = df_cardio['Calories'].fillna(df_cardio['Calories'].mean())
print(df_cardio.info())

#Corelação
print(df_cardio.corr('spearman'))

#Colvariancia
df_cardio.cov()

df_ibov = pd.read_cvs('IBOVDia_05-01-22.CSV', sep=';', skiprows=1, index_col=False)
df_ibov.drop(df_ibov.index[-2:], inplace=True)
df_ibov.tail()

df_ibov.rename(colums={
    'Codigo': 'codigo',
    'Aogigo': 'acao',
    'Qtde. Teorica': 'qtde_teorica',
    'Part. (%)': 'participacao'
}, inplace=True)

df_ibov.describe(include='all')

df_ibov.info()

#Para tratar os dados para numeros
pd.to_numeric(df_ibov['qtde_teorica'])

df_ibov['qtde_teorica'] = df_ibov['qtde_teorica'].str.replace('.', '').astype(float)

df_ibov['participacao'] = df_ibov['participacao'].str.replace(',', '.').astype(float)

print(df_ibov.info())

df_ibov.loc[df_ibov['participacao'] > 5]

df_ibov.iloc[[88, 89]]
df_ibov.describe(include='all')

df_ibov.loc[(df_ibov['participacao']> 2)& (df_ibov['participacao'] < 5)]

df_estatistica = df_ibov.describe(include='all')
type(df_estatistica)

conexao = sql.connect('parte.II.db')
df_estatistica.to_sql('estatistica', conexao)

df_ibov.to_sql('ibov', conexao, if_exists='replace')
df_cardio.to_sql('cardio', conexao, if_exists='replace', index=False)