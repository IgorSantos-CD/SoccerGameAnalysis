from api import fetch_competitions, fetch_seasons, fetch_teams, fetch_standings, fetch_matches, fetch_teams_by_match
from db import insert_competitions, insert_seasons, insert_matches, insert_teams
from supabase_local import connect_to_supabase, define_headers
from dotenv import load_dotenv
from supabase import create_client
import pandas as pd

headers = define_headers()

supabase = connect_to_supabase()

'''#Competições (competitions)
competitions = fetch_competitions(headers)
insert_competitions(supabase, competitions)'''

competitions = supabase.table('competitions').select('id, code').execute()

'''#Temporadas (seasons)
seasons = fetch_seasons(headers, competitions.data)
insert_seasons(supabase, seasons)'''


'''#Matches (jogos)
matches = fetch_matches(headers, competitions.data)
insert_matches(supabase, matches, batch_size=200)
matches = pd.DataFrame(matches)
matches.to_csv('./output/matches/matches.csv', index=False)'''

'''# Teams (times)
teams = fetch_teams_by_match(headers, competitions.data)
teams = pd.DataFrame(teams).drop_duplicates(subset=['id']).to_dict(orient='records')
insert_teams(supabase, teams)'''









