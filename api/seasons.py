import requests
import time
from datetime import datetime

def fetch_seasons(headers, competitions):
    all_seasons = []

    for comp in competitions:
        if comp['code'] in ['WC', 'CL', 'EC', 'CLI']:
            continue

        while True:
            url = f"https://api.football-data.org/v4/competitions/{comp['code']}"
            response = requests.get(url=url, headers=headers)

            if response.status_code == 200:
                competition_data = response.json()
                seasons_data = competition_data['seasons']  # pegar as 6 últimas seasons

                for season in seasons_data:
                    season_entry = {
                        'id': season['id'],
                        'competition_id': comp['id'],
                        'start_date': season['startDate'],
                        'end_date': season['endDate'],
                        'current_matchday': season.get('currentMatchday'),
                        'winner': season['winner']['id'] if season['winner'] else None
                    }
                    all_seasons.append(season_entry)

                break  # sucesso → sai do while

            elif response.status_code == 429:
                print(f"Limite de requisições excedido para {comp['code']}, aguardando 60s...")
                time.sleep(60)  # Espera e tenta de novo

            else:
                raise Exception(f"Erro ao buscar temporada de {comp['code']}: {response.status_code}")

    return all_seasons
