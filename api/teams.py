import requests
import time

def fetch_teams(headers,competitions):
    ids = [competition['code'] for competition in competitions]
    seasons = ['2023','2024','2025']
    teams_infos = []
    for id in ids:
        if id in ['WC', 'CL', 'EC', 'CLI']:
            continue
        
        for season in seasons:
            url = f'https://api.football-data.org/v4/competitions/{id}/teams/?season={season}'
            while True:
                response = requests.get(url=url, headers=headers)

                if response.status_code == 200:
                    data = response.json()
                    teams = data['teams']
                    for team in teams:
                        team_data = {
                            'id': team['id'],
                            'name': team['name'],
                            'short_name': team['shortName'],
                            'tla': team['tla'],
                            'crest_url': team['crest'],
                        }
                        teams_infos.append(team_data)
                    print('Dados dos times coletados com sucesso')
                    break
                elif response.status_code == 429:
                    print(f'Limite de requisições excedido para {id}, aguardando 60s...')
                    time.sleep(60)
                else:
                    print(f'Erro ao obter dados dos times: {id}, {season}, {response.status_code}')
                    raise Exception(f'Não foi possivel obter dados dos times {response.status_code}')
    return teams_infos


def fetch_teams_by_match(headers, competitions):
    ids = [competition['code'] for competition in competitions]
    seasons = ['2023','2024','2025']
    teams_infos = []
    for id in ids:
        for season in seasons:
            if id in ['WC', 'CL', 'EC', 'CLI']:
                continue
            try:
                url = f'https://api.football-data.org/v4/competitions/{id}/matches/?season={season}'
                while True:
                    response = requests.get(url=url, headers=headers)
                    if response.status_code == 200:
                        data = response.json()
                        matches = data['matches']
                        print(len(matches))
                        for match in matches:
                            home_teams_data = {
                                'id': match['homeTeam']['id'],
                                'name': match['homeTeam']['name'],
                                'short_name': match['homeTeam']['shortName'],
                                'tla': match['homeTeam']['tla'],
                                'crest_url': match['homeTeam']['crest'],
                            }
                            away_teams_data = {
                                'id': match['awayTeam']['id'],
                                'name': match['awayTeam']['name'],
                                'short_name': match['awayTeam']['shortName'],
                                'tla': match['awayTeam']['tla'],
                                'crest_url': match['awayTeam']['crest'],
                            }
                            teams_infos.append(home_teams_data)
                            teams_infos.append(away_teams_data)
                        print('Dados dos jogos coletados com sucesso')
                        break
                    elif response.status_code == 429:
                        print(f'Limite de requisições excedido para {id}, aguardando 60s...')
                        time.sleep(60)
                    else:
                        print(f'Erro ao obter dados dos times: {id}, {season}, {response.status_code}')
                        raise Exception(f'Não foi possivel obter dados dos times {response.status_code}')
            except Exception as e:
                print(f'Erro ao obter dados dos times: {id}, {season}, {e}')
                continue
    return teams_infos