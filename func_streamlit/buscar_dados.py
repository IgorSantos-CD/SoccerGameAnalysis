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



