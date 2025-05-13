from api import fetch_competitions, fetch_seasons, fetch_teams
from db import insert_competitions
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

'''#Competições (competitions)
competitions = fetch_competitions(headers)
insert_competitions(supabase, competitions)'''

competitions = supabase.table('competitions').select('*').execute()

#Times (teams)








