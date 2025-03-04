import matplotlib as pyplot
import pandas as pd
import sqlite3 as sql

df_cardio = pd.read_json('Cardio json')

df_ibov = pd.read_cvs('IBOVDia_05-01-22.CSV', sep=';', skiprows=1, index_col=False)

df_cardio.plot()

df_ibov.plot()

df_tempo = pd.read_csv('https://github.com/alanjones2/dataviz/raw/master/londonweather.csv')
df_tempo.head()

df_tempo.info()

df_tempo.to_sql('tempo', conexao, if_exists='replace', index=False)

df_clima_2018 = pd.read_sql('select * from tempo where year = 2018' conexao)
df_clima_2018

df_clima_89 = pd.read_sql('select * from tempo where year = 1989', conexao)
df_clima_89

ax_2018 = df_clima_2018.plot(y='Tmax', marker='o')
ax = df_clima_89.plot(y='Tmax', color='red', ax=ax_2018)
ax.legend(['2018', '1989'])

df_july = pd.read_sql('SELECT * FROM tempo WHERE month == 6', conexao)

df_july.sort_values(by=['Tmax'], ascending=False, inplace=True)

df_july.plot.bar(x='Year', y='Tmax', figsize=(20,5))

import seaborn as sns

sns.set(rc={"figure.figsize": (12, 6)})

sns.distplot(df_july['Tmax'], kde=True)

sns.lmplot(data=df_july, x='Tmax', y='Rain' )
sns.lmplot(data=df_july, x='Tmax', y='Sun')