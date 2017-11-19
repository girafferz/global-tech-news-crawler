import mydb
import fetch
from urllib.request import urlopen
import urllib.request
from bs4 import BeautifulSoup
import re
import hashlib
import pretty
import time


def checkUrl(text):
    return len(text) > 60


def checkTitle(text):
    pattern = r"Partner"
    repatter = re.compile(pattern)
    matchOB = repatter.search(text)

    pattern = r"Etherparty"
    repatter = re.compile(pattern)
    matchOB2 = repatter.search(text)

    if (matchOB is None) and (matchOB2 is None):
        return True
    else:
        return False


def insertWrap(conn, urlMD5, url, siteLogoUrl, articleImageUrl, siteTitleJa, siteTitleRaw, bodyTextJa, bodyTextRaw,
               langCode):
    siteTitleJa = pretty.bodyTextJa(siteTitleJa)
    bodyTextJa = pretty.bodyTextJa(bodyTextJa)
    mydb.insert(conn, urlMD5, url, siteLogoUrl, articleImageUrl, siteTitleJa, siteTitleRaw, bodyTextJa, bodyTextRaw,
                langCode)
    return True


def makeHash(url):
    a = hashlib.md5()
    a.update(url.encode('utf-8'))
    urlMD5 = hashlib.md5(url.encode('utf-8')).hexdigest()
    return urlMD5


def fetchTarget(conn, url):
    host = 'https://www.developer-tech.com/'
    opener = urllib.request.build_opener()
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0"}
    req = urllib.request.Request(url, None, headers)
    data = opener.open(req).read()
    # print(data.decode('utf-8'))
    bsObj = BeautifulSoup(data, "html.parser")
    h1Text = bsObj.h1
    hrefs = bsObj.findAll("a")
    for i in hrefs:
        articleUrl = i["href"]
        result = checkUrl(articleUrl)
        if result == True:
            print('--i.get_text()--')
            print(i.get_text())
            print('article url')
            print(host + articleUrl)
            if i.h2 is not None:
                if checkTitle(i.h2.get_text()) is True:
                    siteTitleJa = fetch.translate_text('ja', i.h2.get_text())
                    siteTitleRaw = i.h2.get_text()
                    bodyTextJa = fetch.translate_text('ja', i.get_text())
                    bodyTextRaw = i.get_text()
                    print(siteTitleJa)
                    print(bodyTextJa)
                    articleImageUrl = 'https://www.developer-tech.com/media/img/news/xgithub_security_vulnerability_developer_warning_l2Ufq5D.jpg.740x370_q96_crop.png.pagespeed.ic.TGLyUxCOb0.jpg'
                    insertWrap(conn, makeHash(host + articleUrl), host + articleUrl, articleImageUrl, articleImageUrl, siteTitleJa, siteTitleRaw, bodyTextJa, bodyTextRaw, 'en')


# main
while True:
    conn = mydb.connect()
    url = 'https://www.developer-tech.com/news/'
    fetchTarget(conn, url)
    time.sleep( 60 * 60 * 24)

