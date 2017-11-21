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


def insertData(conn, title, articleUrl):
    if checkTitle(title) is True:
        siteTitleJa = fetch.translate_text('ja', title)
        siteTitleRaw = title
        bodyTextJa = '(from reddit.com)'
        bodyTextRaw = '(from reddit.com)'
        print('--insert--')
        articleImageUrl = 'https://upload.wikimedia.org/wikipedia/en/thumb/8/82/Reddit_logo_and_wordmark.svg/1200px-Reddit_logo_and_wordmark.svg.png'
        insertWrap(conn, makeHash(articleUrl), articleUrl, articleImageUrl, articleImageUrl, siteTitleJa,
                   siteTitleRaw, bodyTextJa, bodyTextRaw, 'en')


def fetchTarget(conn, url):
    opener = urllib.request.build_opener()
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0"}
    req = urllib.request.Request(url, None, headers)
    data = opener.open(req).read()
    # print(data.decode('utf-8'))
    bsObj = BeautifulSoup(data, "html.parser")
    h1Text = bsObj.h1
    hrefs = bsObj.findAll("a")
    for i in hrefs:
        try:
            articleUrl = i["href"]
            result = checkUrl(articleUrl)
            title = i.parent.get_text()
            if result == True and len(title) > 20:
                print('--58--')
                insertData(conn, title, articleUrl)

        except Exception as e:
            print('--e--')
#            print(e)




# main
while True:
    conn = mydb.connect()
    url = 'https://www.reddit.com/r/programming/new/'
    fetchTarget(conn, url)
    time.sleep( 60 * 60 * 24)

