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
    if checkTitle(text) == False:
        print('--text is ng--')
        print(text)
        return False
    return len(text) > 10


def checkTitle(text):
    pattern = r"asset"
    repatter = re.compile(pattern)
    matchOB = repatter.search(text)

    pattern = r"download"
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


def insertData(conn, title, articleUrl):
    if checkTitle(title) is True:
        siteTitleJa = fetch.translate_text('ja', title)
        siteTitleRaw = title
        bodyTextJa = '(from dzone.com)'
        bodyTextRaw = '(from dzone.com)'
        print('--insert--')
        articleImageUrl = 'https://dzone.com/themes/dz20/images/logo.png'
        insertWrap(conn, makeHash(articleUrl), articleUrl, articleImageUrl, articleImageUrl, siteTitleJa,
                   siteTitleRaw, bodyTextJa, bodyTextRaw, 'en')


def fetchTarget(conn, url):
    opener = urllib.request.build_opener()
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0"}
    req = urllib.request.Request(url, None, headers)
    data = opener.open(req).read()
    t = type(data)
    pattern = r"\"/articles/.*?\""
    matchOB = re.findall(pattern , data.decode('utf-8'))
    print(matchOB)
    hrefs = matchOB
    #bsObj = BeautifulSoup(data, "html.parser")
    #hrefs = bsObj.find_all("div", attrs={"class": "article-title"})
    for i in hrefs:
        try:
            result = checkUrl(i)
            title = i.replace('/articles/', '').replace('-', ' ')
            if result == True and len(title) > 10:
                articleUrl = 'https://dzone.com/' + i.replace('"', '')
                print('--81--')
                print(articleUrl)
                print(title)
                insertData(conn, title, articleUrl)

        except Exception as e:
            print('--e--')
            print(e)




# main
while True:
    conn = mydb.connect()
    url = 'https://dzone.com/devops-tutorials-tools-news/list'
    fetchTarget(conn, url)
    time.sleep( 60 * 60 * 24)

