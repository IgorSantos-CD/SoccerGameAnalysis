from supabase_local import connect_to_supabase
from db import select_supabase
import streamlit as st

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

def media_gols(matches):
    goals_home = []
    goals_away = []
    for matche in matches:
        home = matche['home_score']
        away = matche['away_score']
        goals_home.append(home)
        goals_away.append(away)
    goals_total = sum(goals_home) + sum(goals_away)
    media = round(goals_total/len(matches),2)
    return media





