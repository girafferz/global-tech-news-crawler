from urllib.request import urlopen
from bs4 import BeautifulSoup

import re

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', str(raw_html))
    return cleantext

html = urlopen("https://www.quora.com/Is-Node-js-a-better-choice-than-Python-for-server-side-development-i-e-why-would-one-use-Python-over-Javascript-and-Node-js")
bsObj = BeautifulSoup(html.read(), "html.parser")
print(cleanhtml(bsObj.title))
paras = bsObj.findAll("p", {"class":"qtext_para"})
for hoge in paras:
    print('-------')
    print(cleanhtml(hoge))
