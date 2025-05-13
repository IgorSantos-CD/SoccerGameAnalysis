'''import requests
from dotenv import load_dotenv
import os
import supabase'''

from Functions.fetchs import *

competitions = fetch_competitions()
insert_competitions(competitions)







