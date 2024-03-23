import requests
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
    re = requests.get('https://coinyep.com/api/v1/?from=TON&to=USD&lang=ar&format=json').json()['price']
    send_message(f'{re}$')
    time.sleep(300) # 600 seconds = 5 minutes
