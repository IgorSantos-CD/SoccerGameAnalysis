import requests
import time

def fetch_matches(headers, competitions):
    ids = [competition['code'] for competition in competitions]
    seasons = ['2023','2024','2025']
    matches_infos = []
    for id in ids:
        if id in ['WC', 'CL', 'EC', 'CLI']:
            continue
        for season in seasons:
            try:
                url = f'https://api.football-data.org/v4/competitions/{id}/matches/?season={season}'
                while True:
                    response = requests.get(url=url, headers=headers)
                    if response.status_code == 200:
                        data = response.json()
                        matches = data.get('matches', [])
                        print(f"{len(matches)} jogos encontrados para {id} - {season}")
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
                                'competition_id' : match['competition']['id'],
                            }
                            matches_infos.append(match_data)
                        print('Dados dos jogos coletados com sucesso')   
                        break
                    elif response.status_code == 429:
                        print(f'Limite de requisições excedido para {id}, aguardando 60s...')
                        time.sleep(60)
                    else:
                        raise Exception(f'Não foi possivel obter dados dos times {response.status_code}')
            except Exception as e:
                print(f'Erro ao obter dados dos jogos: {id}, {season}, {response.status_code}')
                continue
    return matches_infos
