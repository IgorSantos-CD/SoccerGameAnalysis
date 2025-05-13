import requests

def fetch_standings(headers,competitions):
    ids = [competition['code'] for competition in competitions]
    for id in ids:
        url = f'https://api.football-data.org/v4/competitions/{id}/standings'
        response = requests.get(url=url, headers=headers)

        if response.status_code != 200:
            raise Exception(f'Não foi possivel obter dados dos times {response.status_code}')
        else:
            data = response.json()
            tabela = data['standings'][0]['table']
            standing_data ={
                'season_id' :  data['season']['id'],
                'curretMatchday' : data['season']['currentMatchday'] 
            }
            print(standing_data)