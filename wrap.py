from bs4 import BeautifulSoup
import requests
import pandas as pd

site = 'https://steamcharts.com/top'
resposta = requests.get(site)
soup = BeautifulSoup(resposta.content, 'html.parser')

resultados = soup.find('table',{'id':'top-games'}).find('tbody').find_all('tr')
nome = []
players_realtime = []
pico_players = []
horas_jogadas = []

for resultado in resultados:
   nome.append(resultado.find('a').get_text().strip())
   players_realtime.append(resultado.find('td',{'class':'num'}).get_text().strip())
   pico_players.append(resultado.find('td',{'class':'num period-col peak-concurrent'}).get_text().strip())
   horas_jogadas.append(resultado.find('td',{'class':'num period-col player-hours'}).get_text().strip())
     
crypto = pd.DataFrame({'Nome':nome, 'Jogadores em tempo real':players_realtime, 
                       'Pico de jogadores':pico_players, 'Horas jogadas':horas_jogadas})
crypto
