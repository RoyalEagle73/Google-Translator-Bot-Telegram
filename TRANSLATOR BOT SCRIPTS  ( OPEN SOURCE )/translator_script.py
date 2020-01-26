import requests

def text(lang="hi", string="i love you"):
    user_agent = "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 Nokia5800d-1/60.0.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.33 Mobile Safari/533.4"
    headers = {'User-Agent':user_agent}
    r = requests.get("https://translate.google.co.in/m?hl=en&sl=auto&tl=%s&ie=UTF-8&prev=_m&q=%s"%(lang,string), headers=headers)
    return (r.text[r.text.find('<div dir="ltr" class="t0">')+len('<div dir="ltr" class="t0">')
    :r.text.find('<',r.text.find('<div dir="ltr" class="t0">')+len('<div dir="ltr" class="t0">')
    )])