import requests
from bs4 import BeautifulSoup
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
    time.sleep(300) # 600 seconds = 5 minute
    rer = requests.get('https://www.okx.com/ar/convert/ton-to-usd').text
    soup = BeautifulSoup(rer, 'html.parser')
    change_container = soup.find('div', class_='index_changeContainer__x0mTX')
    change_percentage = change_container.text.split('(')[1].strip(')')
    price = soup.find('h2', class_='index_price__Yjfiz').text.strip()
    
    send_message(f'''Price: {price}
The Change: {change_percentage}''')
