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

vk_session = vk_api.VkApi('89648268951', 'Maxim161*')
vk_session.auth()
vk = vk_session.get_api()

while True:
    with open('att.txt', 'r') as f:
        attrs = f.read().splitlines()
    try:
        print(f'posting photo')
        text, author = get_quote()
        vk.wall.post(owner_id = -192839261, from_group=1, attachments = attrs[0], message = text + '\n\n©' + author)
        attrs.pop(0)
        with open('att.txt', 'w') as f:
            f.write('\n'.join(attrs))
        sleep(180)
    except Exception as e:
        print(e)
        continue
