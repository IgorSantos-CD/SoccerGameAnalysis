from dotenv import load_dotenv
from supabase import create_client 
import os

def connect_to_supabase():
    load_dotenv('./.env')
    
    SUPABASE_URL = os.getenv("SUPABASE_URL")
    SUPABASE_KEY = os.getenv("SUPABASE_KEY")
    
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
    
    return supabase

def define_headers():
    load_dotenv('./.env')
    
    API_TOKEN = os.getenv("API_TOKEN") #Obtendo chave de API do arquivo .env
    
    #Configurando o header da requisição, isso que vai liberar o acesso à API
    headers ={
        "X-Auth-Token" : API_TOKEN
    }
    
    return headers