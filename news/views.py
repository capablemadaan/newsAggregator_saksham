from django.shortcuts import render

# Create your views here.
import requests
from bs4 import BeautifulSoup
# trendings
toi_t_r = requests.get("https://timesofindia.indiatimes.com/briefs")  # toi_t_r =times of india trnding r
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
# trendings



# home affairs

toi_ha_r = requests.get("https://timesofindia.indiatimes.com/india")
toi_ha_soup = BeautifulSoup(toi_ha_r.content, 'html.parser')
toi_ha_headings = toi_ha_soup.find_all('li')
toi_ha_headings=toi_ha_headings[76:136]
toi_ha_news=[]
for th in toi_ha_headings:
    toi_ha_news.append(th.text)

tt_har = requests.get("https://www.tribuneindia.com/news/nation")
tt_hasoup = BeautifulSoup(tt_har.content, 'html.parser')
tt_haheadings = tt_hasoup.findAll("a", {"class": "card-top-align"})
#tt_theadings = tt_theadings[2:]
tt_hanews = []
for hth in tt_haheadings:
    tt_hanews.append(hth.text)
# home affairs


# foregein affairs
toi_fa_r = requests.get("https://timesofindia.indiatimes.com/world")
toi_fa_soup = BeautifulSoup(toi_fa_r.content, 'html.parser')
toi_fa_headings = toi_fa_soup.find_all('li')
toi_fa_headings=toi_fa_headings[43:93]
toi_fa_news=[]
for th in toi_fa_headings:
    toi_fa_news.append(th.text)

tt_far = requests.get("https://www.tribuneindia.com/news/world")
tt_fasoup = BeautifulSoup(tt_far.content, 'html.parser')
tt_faheadings = tt_fasoup.findAll("a", {"class": "card-top-align"})
#tt_theadings = tt_theadings[2:]
tt_fanews = []
for hth in tt_faheadings:
    tt_fanews.append(hth.text)
# foregein affairs


# business section
bi_b_r=requests.get("https://www.businessinsider.in/business/startups")
bi_bsoup=BeautifulSoup(bi_b_r.content,'html.parser')
bi_bheadings=bi_bsoup.findAll("span",{"class":"liststories_heading"})
bi_bnews=[]
for h in bi_bheadings:
    bi_bnews.append(h.text)  

tc_b_r=requests.get("https://techcrunch.com/startups/")
tc_bsoup=BeautifulSoup(tc_b_r.content,'html.parser')
tc_bheadings=tc_bsoup.findAll("h2",{"class":"post-block__title"})
tc_bnews=[]
for h in tc_bheadings:
    tc_bnews.append(h.text)
# business section  



# dtu section  
dtu_r = requests.get("http://dtu.ac.in/")
dtu_soup = BeautifulSoup(dtu_r.content, 'html.parser')
dtu_headings = dtu_soup.findAll("a", {"class":"colr"})
dtu_headings = dtu_headings[23:43]
dtu_news = []
for hth in dtu_headings:
    dtu_news.append(hth.text)
# dtu section


# sports section
iex_s_r=requests.get("https://indianexpress.com/section/sports/")
iex_ssoup=BeautifulSoup(iex_s_r.content,'html.parser')
iex_sheadings=iex_ssoup.findAll("h2",{"class":"title"})
iex_snews=[]
for h in iex_sheadings:
    iex_snews.append(h.text)

itn_s_r=requests.get("https://www.thenews.com.pk/latest/category/sports")
itn_ssoup=BeautifulSoup(itn_s_r.content,'html.parser')
itn_sheadings=itn_ssoup.findAll("h2")
itn_sheadings = itn_sheadings[1:]
itn_snews=[]
for h in itn_sheadings:
    itn_snews.append(h.text)    
# sports section


#  snt section
# snt section here
#  snt section
def index(req):
    return render(req, 'news/home.html')
def index1(req):
    return render(req, 'news/trending.html',{'toi_t_news':toi_t_news, 'tt_tnews': tt_tnews})
def index2(req):
    return render(req, 'news/homeaffairs.html',{'toi_t_news':toi_ha_news, 'tt_tnews': tt_hanews})
def index3(req):
    return render(req, 'news/fa.html',{'toi_t_news':toi_fa_news, 'tt_tnews': tt_fanews})
def index4(req):
    return render(req, 'news/sports.html',{'iex_snews':iex_snews,'itn_snews':itn_snews})
def index5(req):
    return render(req, 'news/snt.html')
def index6(req):
    return render(req, 'news/busi.html',{'bi_bnews':bi_bnews,'tc_bnews':tc_bnews})
def index7(req):
    return render(req, 'news/dtu.html', {'dtu_news':dtu_news})

