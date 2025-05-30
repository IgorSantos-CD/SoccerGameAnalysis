import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from db import select_supabase
from supabase_local import connect_to_supabase, define_headers
from func_streamlit import (year_validate, big_number_card,plotar_contagem, rodadas_disputadas, media_gols, formatar_placares,
                            plotar_pizza, formatar_resultados)

# Connect to Supabase
supabase = connect_to_supabase()
headers = define_headers()

st.set_page_config(page_title="Soccer Analysis", page_icon="⚽", layout="wide")

## TRAZENDO AS COMPETIÇÕES DO BANCO DE DADOS
competitions = select_supabase(supabase, 'competitions', '*')

## TITULO DA SIDEBAR
st.sidebar.title('Soccer Analysis')

## CRIANDO FILTRO E ARMAZENANDO A ESCOLHA DO USUÁRIO
competicoes_disponiveis = {name : comp_id for code, name , comp_id in competitions[['code','name','id']].values if code not in ['WC', 'CL', 'EC', 'CLI']}
competicao = st.sidebar.selectbox('Selecione a competição:',competicoes_disponiveis)
cod_comp = competicoes_disponiveis[competicao]

## BUSCANDO AS TEMPORADAS NO BANCO DE DADOS 
seasons = select_supabase(supabase, 'seasons', '*', [{'coluna':'competition_id', 'operador':"eq", 'valor':cod_comp}])
ids_temp = {start_date : season_id for season_id, start_date in seasons[['id','start_date']].values}

## VALIDANDO AS TEMPORADAS ONDE TEMOS JOGOS NO BANCO DE DADOS
#Necessário validar para melhorar a experiencia do usuário e não possibilitar filtros de ligas vazias
ids_validos = {}
for start_date, id_temp in ids_temp.items():
    df = select_supabase(supabase, 'matches', 'id', [{'coluna':'season_id', 'operador':'eq', 'valor':id_temp}])
    if len(df) > 0:
        ids_validos[start_date] = id_temp

## GUARDANDO SELEÇÃO DO USUÁRIO
anos = [int(ano[:4]) for ano in ids_validos.keys()]
ano_selecionado = st.sidebar.slider('Selecione a temporada:', min_value=min(anos), max_value=max(anos))

## BUSCANDO O ID DA TEMPORADA SELECIONADA
for start_date, id_temp in ids_validos.items():
    if int(start_date[:4]) == ano_selecionado:
        id_escolhido = id_temp

st.markdown(f'## :soccer: {competicao} | {ano_selecionado}')
st.markdown('---')

## BUSCANDO AS PATIDAS DA LIGA E DA TEMPORADA SELECIONADA
matches = select_supabase(supabase, 'jogos_com_detalhes','*',[{'coluna':'season_id', 'operador':'eq','valor':id_escolhido}])

#GERANDO COLUNAS PARA APRESENTAÇÃO DE DADOS (BIG_NUMBERS)
col1, col2, col3, col4 = st.columns(4)
media_total, jogos_total, gols_total = media_gols(matches)

## COLUNA 1 - RODADAS DISPUTADAS
with col1:
    big_number_card('Rodadas Disputadas', max(matches['current_matchday']))

## COLUNA 2 - QUANTIDADE DE JOGOS DISPUTADOS
with col2:
    big_number_card('Partidas Disputadas', jogos_total)

## COLUNA 3 - TOTAL DE GOLS MARCADOS NA COMPETIÇÃO/TEMPORADA
with col3:
    big_number_card('Total de Gols Marcados', gols_total)

## COLUNA 4 - MEDIA DE GOLS POR JOGO NA COMPETIÇÃO/TEMPORADA
with col4:
    big_number_card('Media de Gols por Jogo:', media_total)

st.markdown('---')

## GERANDO COLUNA PARA APRESENTAÇÃO DE DADOS (DISTRIBUIÇÃO DE DADOS)
col1, col2 = st.columns(2)

## TRATANDO PLACARES
placares = matches[['home_score','away_score']].loc[matches['status']=='FINISHED'].copy()
placares['placar'] = placares.apply(formatar_placares, axis=1)

## TRATANDO RESULTADOS
resultados = matches[['winner']].loc[matches['status']=='FINISHED'].copy()
resultados['Vencedor'] = resultados.apply(formatar_resultados, axis=1)

## COLUNA 1 - 5 PLACARES MAIS COMUNS NO CAMPEONATO
with col1:
    st.markdown('### Placares mais comuns')
    fig = plotar_contagem(placares, 'placar')
    st.pyplot(fig)

## COLUNA 2 - DISTRIBUIÇÃO DE RESULTADOS DO CAMPEONATO
with col2:
    st.markdown("### Distribuição de resultados")
    fig = plotar_pizza(resultados, 'Vencedor')
    st.pyplot(fig)

st.markdown('---')
st.markdown('### Clubes da competição')
st.markdown('')

# SELECIONANDO OS LINKS SEM DUPLICADAS DOS CLUBES
home_crests = matches[['home_team_name', 'home_team_crest_url']].drop_duplicates()
away_crests = matches[['away_team_name', 'away_team_crest_url']].drop_duplicates()

# RENOMEAR PARA FACILITAR A CONCATENAÇÃO
home_crests.columns = ['team_name', 'crest_url']
away_crests.columns = ['team_name', 'crest_url']

# CONCATENAR E REMOVER DUPLICADAS
all_crests = pd.concat([home_crests, away_crests]).drop_duplicates(subset='team_name').reset_index(drop=True)

# DEFINE O NUMERO DE COLUNAS DESEJADO POR GRID
cols = st.columns(5, gap='large')

for idx, row in all_crests.iterrows():
    col = cols[idx % 5]  # Escolhe a coluna de forma cíclica
    with col:
        st.image(row['crest_url'], width=80, caption=row['team_name'])

times_casa = matches[['home_team_short_name','home_score','away_score']].rename(
    columns={'home_team_short_name':'time','home_score':'gols_pro','away_score':'gols_contra'}
    )

times_fora = matches[['away_team_short_name','home_score','away_score']].rename(
    columns={'away_team_short_name':'time','home_score':'gols_contra','away_score':'gols_pro'}
    )

times = pd.concat([times_casa,times_fora])


