import requests
import time
'''
    Função para buscar os dados de classificação de uma competição específica.
    Ainda não está implementada, mas a ideia é que ela faça uma requisição para a API
    e retorne os dados de classificação.
    '''

def fetch_standings(headers,competitions):
    ids = [competition['code'] for competition in competitions]
    standings = []
    for id in ids:
        while True:
            url = f'https://api.football-data.org/v4/competitions/{id}/standings'
            response = requests.get(url=url, headers=headers)

            if response.status_code == 200:
                data = response.json()
                tabela = data['standings'][0]['table']
                standing_data ={
                    'season_id' :  data['season']['id'],
                    'curretMatchday' : data['season']['currentMatchday'] 
                }
                print('Dados da temporada coletados com sucesso')
                standings.append(standing_data)

                break  # sucesso → sai do while
            elif response.status_code == 429: 
                print(f'Limite de requisições excedido para {id}, aguardando 60s...')
                time.sleep(60)            
            else:
              raise Exception(f'Não foi possivel obter dados dos times {response.status_code}')
    return standings
    