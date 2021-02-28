from django.shortcuts import render

# Create your views here.
import requests
from bs4 import BeautifulSoup

toi_r = requests.get("https://timesofindia.indiatimes.com/briefs")
toi_soup = BeautifulSoup(toi_r.content, 'html5lib')
toi_headings = toi_soup.find_all('h2')
toi_headings=toi_headings[2:-13]
toi_news=[]
for th in toi_headings:
    toi_news.append(th.text)

ht_r = requests.get("https://www.tribuneindia.com/news/nation")
ht_soup = BeautifulSoup(ht_r.content, 'html5lib')
ht_headings = ht_soup.findAll("h4", {"class": "ts-card-title"})
#ht_headings = ht_headings[2:]
ht_news = []
for hth in ht_headings:
    ht_news.append(hth.text)

def index(req):
    return render(req, 'news/trending.html',{'toi_news':toi_news, 'ht_news': ht_news})