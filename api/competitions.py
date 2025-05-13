import requests
import os

def fetch_competitions(headers):
    url = "https://api.football-data.org/v4/competitions/"
    response = requests.get(url=url, headers=headers)

    if response.status_code != 200:
        raise Exception(f'Erro ao buscar as competições: {response.status_code}')
    return response.json()["competitions"]









