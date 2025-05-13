import requests

def fetch_seasons(headers, competitions):
    ids = [competition['code'] for competition in competitions]
    for id in ids:
        url = f'http://api.football-data.org/v4/competitions/{id}'
        response = requests.get(url, headers)

        if response.status_code != 200:
            raise Exception(f'Não foi possivel obter dados da temporada {response.status_code}')
        else:
            competition_data = response.json()
            seasons = [competition_data['seasons']]
            season_id = [season['id'] for season in seasons]
            print(season_id)