from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv
from google.colab import drive
from time import sleep
import datetime

drive.mount('/drive')
while True:
  site = 'https://steamcharts.com/top'
  resposta = requests.get(site)
  soup = BeautifulSoup(resposta.content, 'html.parser')
  resultados = soup.find('table',{'id':'top-games'}).find('tbody').find_all('tr')
  for resultado in resultados:
    nome=(resultado.find('a').get_text().strip())
    players_realtime=(resultado.find('td',{'class':'num'}).get_text().strip())
    pico_players=(resultado.find('td',{'class':'num period-col peak-concurrent'}).get_text().strip())
    horas_jogadas=(resultado.find('td',{'class':'num period-col player-hours'}).get_text().strip())
    linha = str('Nome 🎮:'+nome +'|'+'Jogadores realtime: 🫂' + players_realtime + '|' + 'Pico: 📈'+ pico_players + '|'+'Horas jogadas: ⏰' + horas_jogadas).strip()
    steam = open('/drive/My Drive/csv/steam.csv','a', encoding="UTF8")
    writer = csv.writer(steam, escapechar='', quoting=csv.QUOTE_NONE)
    writer.writerow([linha])
    steam.close()
  sleep(10)
   