import requests
import json
import time
#from requests.exceptions import HTTPError


with open('countries.json', 'r') as f:
    dic = json.load(f)

def convert_country_code(name):
    return dic['code3'][name]

def request_news(keyword):
    q = '''https://api.gdeltproject.org/api/v2/doc/doc?query="{}"%20&mode=artlist&maxrecords=200&timespan=3d&sort=datedesc&format=json'''
    res = requests.get(q.format(keyword))
    if res.status_code == 200:
        try:
            articles = json.loads(res.content)
            return articles["articles"]
        except:
            pass
    return None

def crawl_news(keywords):
    for k in keywords:
        articles = request_news(k.replace(' ', '%20'))
        if not articles or len(articles) == 0:
            continue
        print(k, len(articles), sep='\t')
        for d in articles:
            try:
                d['country'] = convert_country_code(d['sourcecountry'])
            except:
                pass
        with open('data/news/{}.json'.format(k.replace(' ', '_')), 'w') as f:
            json.dump(articles, f)

with open('keywords.txt', 'r') as f:
    crawl_news([_.strip() for _ in f.readlines()])


