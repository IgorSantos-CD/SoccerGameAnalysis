import requests
from dotenv import load_dotenv
import os
import supabase

load_dotenv('./.env')

API_TOKEN = os.getenv("API_TOKEN") #Obtendo chave de API do arquivo .env

#Configurando o header da requisição, isso que vai liberar o acesso à API
headers ={
    "X-Auth-Token" : API_TOKEN
}

url = "https://api.football-data.org/v4/competitions/"

response = requests.get(url=url, headers=headers)

if response.status_code == 200:
    print("Requisição bem-sucedida")
    data = response.json()
    print(data)

    for i, comp in enumerate(data['competitions']):
        print(f'{i+1}. {comp['name']} - Area_code: {comp['area']['code']} ({comp['code']})')
else:
    print(f'Erro: {response.status_code}')







