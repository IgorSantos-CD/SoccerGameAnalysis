import requests
import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv('./.env')

API_TOKEN = os.getenv("API_TOKEN") #Obtendo chave de API do arquivo .env

#Configurando o header da requisição, isso que vai liberar o acesso à API
headers ={
    "X-Auth-Token" : API_TOKEN
}


SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)



def fetch_competitions():
    url = "https://api.football-data.org/v4/competitions/"
    response = requests.get(url=url, headers=headers)

    if response.status_code != 200:
        raise Exception(f'Erro ao buscar as competições: {response.status_code}')
    return response.json()["competitions"]

def insert_competitions(base):
    for comp in base:
        comp_data = {
            "id" : comp['id'],
            "name" : comp['name'],
            "code" : comp['code'],
            "area_name" : comp['area']['code']
        }

        existing = supabase.table('competitions').select("id").eq('id',comp_data['id']).execute()
        if len(existing.data) == 0:
            supabase.table('competitions').insert(comp_data).execute()
            print("Competição incluida com sucesso")
        else:
            print(f'Competição {comp_data["name"]} já existe no banco')








