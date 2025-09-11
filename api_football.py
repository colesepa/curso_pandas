import requests
import json 
import pandas as pd

uri = 'https://api.football-data.org/v4/competitions'

response = requests.get(uri)        