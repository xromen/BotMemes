import vk_api
from os import getcwd
from time import sleep
import requests


def get_quote():
    #print('Parsing quote')
    res = requests.post(url='http://api.forismatic.com/api/1.0/', data = {'method':'getQuote', 'format' : 'json'})
    quoteText = res.json()['quoteText']
    quoteAuthor = res.json()['quoteAuthor']
    return quoteText, quoteAuthor

text, author = get_quote()
print(text)
print(author)

vk_session = vk_api.VkApi('89648268951', 'Maxim161*')
vk_session.auth()
vk = vk_session.get_api()

with open('att.txt', 'r') as f:
    attrs = f.read().splitlines()

for i, x in enumerate(attrs):
    try:
        print(f'posting {i} photo')
        text, author = get_quote()
        vk.wall.post(owner_id = -192839261, from_group=1, attachments = x, message = text + '\n\n©' + author)
        sleep(180)
    except Exception as e:
        print(e.__class__)
        continue
