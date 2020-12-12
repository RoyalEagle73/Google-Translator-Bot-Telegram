import requests
from bs4 import BeautifulSoup

def text(lang="hi", string="i love you"):
    user_agent = "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 Nokia5800d-1/60.0.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.33 Mobile Safari/533.4"
    headers = {'User-Agent':user_agent}
    r = requests.get("https://translate.google.co.in/m?sl=auto&tl=%s&q=%s&hl=en-US"%(lang,string), headers=headers)
    soup = BeautifulSoup(r.text, "lxml")
    return soup.find("div", attrs={"class":"result-container"}).text