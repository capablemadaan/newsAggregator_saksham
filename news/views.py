from django.shortcuts import render

# Create your views here.
import requests
from bs4 import BeautifulSoup

toi_t_r = requests.get("https://timesofindia.indiatimes.com/briefs")
toi_t_soup = BeautifulSoup(toi_t_r.content, 'html.parser')
toi_t_headings = toi_t_soup.find_all('h2')
toi_t_headings=toi_t_headings[2:-13]
toi_t_news=[]
for th in toi_t_headings:
    toi_t_news.append(th.text)

tt_tr = requests.get("https://www.tribuneindia.com/")
tt_tsoup = BeautifulSoup(tt_tr.content, 'html.parser')
tt_theadings = tt_tsoup.findAll("a", {"class": "card-top-align"})
#tt_theadings = tt_theadings[2:]
tt_tnews = []
for hth in tt_theadings:
    tt_tnews.append(hth.text)

def index(req):
    return render(req, 'news/home.html')
def index1(req):
    return render(req, 'news/trending.html',{'toi_t_news':toi_t_news, 'tt_tnews': tt_tnews})
# def index2(req):
#     return render(req, 'news/homeaffairs.html',)
# def index3(req):
#     return render(req, 'news/foreignaffairs.html',)
# def index4(req):
#     return render(req, 'news/sports.html',)
# def index5(req):
#     return render(req, 'news/snt.html')
# def index6(req):
#     return render(req, 'news/busi.html')
# def index7(req):
#     return render(req, 'news/dtu.html')