import pandas as pd
import sqlite3 as sql

df_cardio = pd.read_json('Cardio json')
print(df_cardio)

print(type(df_cardio))

print(type(df_cardio['calories']))

print(type(df_cardio.index))

df_cardio.head()