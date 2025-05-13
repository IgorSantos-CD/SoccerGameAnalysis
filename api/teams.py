import requests


def fetch_teams(headers,competitions):
    ids = [competition['code'] for competition in competitions]
    for id in ids:
        url = f'https://api.football-data.org/v4/competitions/{id}/teams'
        response = requests.get(url, headers)

        if response.status_code != 200:
            raise Exception(f'Não foi possivel obter dados dos times {response.status_code}')
        else:
            print(response.json())
