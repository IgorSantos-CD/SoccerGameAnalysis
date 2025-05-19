import pandas as pd
import streamlit as st
from supabase_local import connect_to_supabase, define_headers

# Connect to Supabase
supabase = connect_to_supabase()
headers = define_headers()

st.set_page_config(page_title="Soccer Analysis", page_icon="⚽", layout="wide")

st.title("Soccer Analysis")
st.subheader("Data from Soccer API")

# Fetch competitions data
competitions = supabase.table('competitions').select('id, code').execute()
competitions = pd.DataFrame(competitions.data)

# Display competitions data
st.write("## Competitions")
st.write(competitions)
