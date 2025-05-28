from supabase_local import connect_to_supabase
from db import select_supabase
import streamlit as st
import pandas as pd

supabase = connect_to_supabase()

@st.cache_data
def year_validate(years, liga_id):
    years_not_null = {}
    for year, season_id in years.items():
        matches = select_supabase(supabase, 'matches', '*',{'season_id' :season_id, 'status' : 'FINISHED', 'competition_id':liga_id})
        if matches:
            years_not_null[year] = season_id
    return years_not_null


def rodadas_disputadas(competition, season):
    current_matchday = select_supabase(supabase, 'seasons', 'current_matchday',{'id' : season, 'competition_id' : competition})
    rodada_atual = current_matchday[0]['current_matchday']
    return rodada_atual

def media_gols(df):
    df_not_null = df.loc[
        (pd.notnull(df['home_score'])) & 
        (pd.notnull(df['away_score'])) & 
        (df['status'] == 'FINISHED')
    ]
    gols_total = int(sum(df_not_null['home_score']) + sum(df_not_null['away_score']))
    jogos_total = int(df_not_null.shape[0])
    media = round(gols_total/jogos_total,2)
    return media, jogos_total, gols_total

def formatar_placares(row):
    gol_casa = int(row['home_score'])
    gol_fora = int(row['away_score'])
    placar = f'{gol_casa} x {gol_fora}'
    return placar





