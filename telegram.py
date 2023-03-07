#TELEGRAM BOT @steamtrendsbot

import requests
import pandas as pd
from time import sleep

path = "/content/drive/MyDrive/csv/steam.csv"
df = pd.read_csv(path)


def send_msg(text):
  token = ""
  chat_id = ""
  url_req = "https://api.telegram.org/bot"+ token +"/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
  results = requests.get(url_req)
 
while True:
 send_msg(df.to_string())
 sleep(1)