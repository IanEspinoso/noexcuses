## Main imports
import requests
import pandas as pd

## Get the API key

#with open("api_token.txt", "r", encoding="utf-8") as file:
#    contents = file.read().strip()  # .strip() removes spaces/newlines

#print(contents)

## Pull API data

api_key = '5d16028f-0270-4ff3-8731-ec78a9259b72'

buscar_area_act_method = 'https://www.inegi.org.mx/app/api/denue/v1/consulta/'
buscar_area_act_method += 'BuscarAreaAct/00/0/0/0/0/0/0/0/713943/0/1/999999999/0/'

## Use requests method

url_requested = buscar_area_act_method + api_key

header = {
    "accept": "*/*",
    "Authorization": api_key
}

response = requests.get(url_requested, headers=header)

data = response.json()

df = pd.json_normalize(data)

pd.to_csv("mexico_gyms.csv", index=False, encoding='utf-8')