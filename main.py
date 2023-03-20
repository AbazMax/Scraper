import requests
from bs4 import BeautifulSoup
import time

token = 'Your_telegram_bot_token'
channel_id = '@Your_channel_name'
flag = True

def parcer():
    page = requests.get('https://www.tesmanian.com/')
    soup = BeautifulSoup(page.text, 'html.parser').main
    articles = []
    if page.status_code == 200:
        article_elements = soup.find_all('div', class_='gap-3')
        for el in article_elements:
            link = el.find('a')
            articles.append({
                'title': link.text,
                'link': f'https://www.tesmanian.com/{link.get("href")}'
            })
        return articles
    else:
        print(page.status_code)


def post_message(message):
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    response = requests.get(url, {
         "chat_id": channel_id,
         "text": message
          })
    if response.status_code == 200:
        print('ok')
    else:
        print(response.text)


while flag == True:
    article_list = parcer()
    for el in article_list:
        post_message(f'{el["title"]} - {el["link"]}')
        time.sleep(15)

