#%%
import pandas as pd

# %%
idades = [32, 35, 47, 52, 36, 47, 12 ,36, 69, 78]

#%%
idades_series = pd.Series(idades)
# %%
idades_series.var
# %%

idades_series.describe()

# %%

idades_series[0:3]
# %%
"""Os indices das séries funcionam como chaves de dicionario
O index de um elemento fica associoado a um valor da série como se fosse
um ID. 
Mas podemos resetar o index.

df.iloc[] -> POSIÇÃO DE UM ELEMENTO DE UMA SÉRIE

"""

idades_series.iloc[-1]

# %%
"""Podemos setar os index """

index = [
    'Matheus', 'José', 'Andrade', 'Ramon',
    'Flavia', 'Maria', 'Fernanda', 'Theo', 
    'Thomaz', 'Katia']

series_com_index = pd.Series(idades, index=index)
# %%
series_com_index
# %%

series_com_index['Matheus':'Flavia':3] #-> Navega pelos indices pulando de 3 em 3
series_com_index['Matheus':'Flavia'] #-> Navega pelos indices

# %%
idades = [32, 35, 47, 52, 36, 47, 12 ,36, 69, 78]
nomes = ['Matheus', 'José', 'Andrade', 'Ramon', 'Flavia', 
         'Maria', 'Fernanda', 'Theo', 'Thomaz', 'Katia']

series_idades = pd.Series(idades)
series_nomes = pd.Series(nomes)
# %%
df = pd.DataFrame()
df['Idades'] = series_idades
df['nomes'] = series_nomes

df
# %%

df['nomes']
# %%
