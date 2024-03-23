import requests
try:
 import time
except ModuleNotFoundError:
 import os
 os.system("pip install -r requirements.txt")

import time

api_key = '7077041742:AAGueuEPoethOJ2U2BFCbYVfyKVqYmBqX1k'
channel_username = '@Ton_Pricee'

def send_message(message):
    url = f'https://api.telegram.org/bot{api_key}/sendMessage'
    params = {
        'chat_id': channel_username,
        'text': message
    }
    response = requests.post(url, params=params)

while True:
    text = requests.get('https://www.okx.com/ar/convert/ton-to-usd').text
    dd =text.split('اليوم TON إلى USD هو')[1]
    rr = dd.split('."}},{"@type"')[0]
    send_message(f'{rr}')
    time.sleep(300) # 600 seconds = 5 minutes
