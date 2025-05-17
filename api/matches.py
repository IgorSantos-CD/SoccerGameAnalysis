import requests
import time

def fetch_matches(headers, competitions):
    #ids = [competition['code'] for competition in competitions]
    ids = ['BSA']
    matches = []
    for id in ids:
        while True:
            url = f'https://api.football-data.org/v4/competitions/{id}/matches'
            response = requests.get(url=url, headers=headers)

            if response.status_code == 200:
                data = response.json()
                matches = data['matches']
                for match in matches:
                    match_data = {
                        'id': match['id'],
                        'season_id': match['season']['id'],
                        'utc_date' : match['utcDate'],
                        'status' : match['status'],
                        'matchday' : match['season']['currentMatchday'],
                        'home_team_id' : match['homeTeam']['id'],
                        'away_team_id' : match['awayTeam']['id'],
                        'home_score' : match['score']['fullTime']['home'],
                        'away_score' : match['score']['fullTime']['away'],
                        'winner' : match['score']['winner'],
                        'competitions_id' : match['competition']['id'],
                    }
                print('Dados dos jogos coletados com sucesso')
                matches.append(match_data)
                break  # sucesso → sai do while
            elif response.status_code == 429:
                print(f'Limite de requisições excedido para {id}, aguardando 60s...')
                time.sleep(60)
            else:
                raise Exception(f'Não foi possivel obter dados dos times {response.status_code}')
    return matches
