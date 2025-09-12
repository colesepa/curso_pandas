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
"""Os indices das séries funcionam como chaves de dicionario"""

idades_series[]

# %%
