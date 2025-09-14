#%%

import pandas as pd

# %%
#Importando arquivos csv

df = pd.read_csv('../data/clientes.csv',sep=';')
# %%
df
# %%

df.to_csv('clientes.csv',index=False)
# %%
df.to_json('clientes.json',indent=4, index=False)
# %%
df.head(10) #Mostra as 10 primeira linhas da df
# %%
df.tail(10)#Mostas as 10 ultimas linhas da df
# %%
df.sample(10) #mostas 10 linhas de posições aleatórias do data frame  
# %%
df.shape #Atributo do datafrema retrornando uma tupla com numero de linhas e colunas
# %%

df.columns #nomes das colunas

# %%
df.index
# %%
df.info(memory_usage='deep')
# %%

df.dtypes # -> É uma série do pandas
# %%
df['IdCliente'].dtypes # -> Retorna o tipo de objetct dentro da serie O == Objetcts
# %%
df.dtypes['FlEmail'] # -> Retorna o tipo de obejto da série Int64


# %%
"""
Renomear colunas 

df.rename(columns={'<nome_antigo':<nome_novo>}, inplace=True)
df = df.rename(columns={'<nome_antigo':<nome_novo>})

Visualizar varios elementos de um dataFrame

df["<nome_da_coluna"] -> Retorna uma série da <nome_coluna>
df[["<nome_da_coluna_1"], ["<nome_da_coluna_2"]] -> Retorna um DF com duas colunas
df[["<nome_da_coluna_1"]] -> Retorna uma DF com uma única coluna

"""

df.columns
# %%

df.rename(columns={'IdCliente':'id_cliente'}, inplace=True)
# %%
df.head(5)
# %%
df['id_cliente']
# %%
df[['id_cliente']]
# %%
df[['id_cliente','QtdePontos']]

# %%
