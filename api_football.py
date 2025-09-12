#%%
import requests
import json
import pandas as pd
from tqdm import tqdm

uri = 'https://api.football-data.org/v4/competitions'

response = requests.get(uri) 
if response.status_code == 200:
    dados = response.json()

dados = dados['competitions']
competition = dados[8]

# %%
columns = list(competition.keys())
for col in columns:
    info = '{col}: {competition[col]}'
    print(f'{col}: {competition[col]}')
    
# %%
brazilian_leagues = []
for competition in dados:
    if competition['area']['name'] == 'Brazil':
        brazilian_leagues.append(competition)
# %%
len(brazilian_leagues)
