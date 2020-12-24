import vk_api
from os import getcwd
from time import sleep
import requests
from random import choice


def get_quote():
    #print('Parsing quote')
    res = requests.post(url='http://api.forismatic.com/api/1.0/', data = {'method':'getQuote', 'format' : 'json'})
    quoteText = res.json()['quoteText']
    quoteAuthor = res.json()['quoteAuthor']
    return quoteText, quoteAuthor

vk_session = vk_api.VkApi('89648268951', 'MAximus74@')
vk_session.auth()
vk = vk_session.get_api()

groups = ['amfet1', 'prukl', 'publicepsilon777', 'pozvk', 'fun_club_sponge_bob_mem', 'prucl', 'intellectualmems', 'gifsvine', 'oldy_zdez']
attrs = []

while 1:
    try:
        wall = vk.wall.get(domain=choice(groups), count=10)['items']
        post_id = max({i['id'] : i['likes']['count'] for i in wall})
        post = [i for i in wall if i['id']==post_id]
        #print(post)
        atts = ''
        for i in post[0]['attachments']:
            if i['type']!='photo':
                continue
            if atts:
                atts+=','
            atts += 'photo'+str(i['photo']['owner_id'])+'_'+str(i['photo']['id'])
        if not atts in attrs:
            print(atts)
            print(vk.wall.post(owner_id = -192839261, from_group=1, attachments = atts))
            attrs.append(atts)
        else:
            continue
        if len(attrs)>20:
            attrs.pop(0)
    except:
        continue
    sleep(1800)
