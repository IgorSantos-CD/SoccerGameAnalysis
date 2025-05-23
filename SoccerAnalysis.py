import pandas as pd
import streamlit as st
from db import select_supabase
from supabase_local import connect_to_supabase, define_headers

# Connect to Supabase
supabase = connect_to_supabase()
headers = define_headers()

st.set_page_config(page_title="Soccer Analysis", page_icon="⚽", layout="wide")

competitions = select_supabase(supabase, 'competitions', 'name, code, id')

comp_name_code = {item['name']:item['id'] for item in competitions if item['code'] not in ['WC', 'CL', 'EC', 'CLI']}

st.sidebar.title('Filtros')
liga = st.sidebar.selectbox('Selecione a competição que deseja visualizar:', list(comp_name_code.keys()))
liga_id = comp_name_code[liga]

seasons_available = select_supabase(supabase, 'seasons', 'id, start_date, end_date', condicao={'competition_id':liga_id})
years = {item['start_date'][:4] : item['id'] for item in seasons_available}
years_list = [int(y) for y in years]
season = st.sidebar.slider('Selecione a Temporada:', min(years_list), max(years_list))
select_season = next(
    (item['id'] for item in seasons_available if item['start_date'][:4] == str(season)),
    None  # valor padrão se não encontrar
)

matches = select_supabase(supabase, 'matches', '*',{'season_id':select_season, 'status':'FINISHED','competition_id':liga_id})

st.write(matches)