import mydb
import fetch
from urllib.request import urlopen
import urllib.request
from bs4 import BeautifulSoup
import re
import hashlib
import pretty


def checkUrl(text):
    return len(text) > 80


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


def fetchMedium(conn, url):
    opener = urllib.request.build_opener()
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0"}
    req = urllib.request.Request(url, None, headers)
    data = opener.open(req).read()
    # print(data.decode('utf-8'))

    bsObj = BeautifulSoup(data, "html.parser")
    h1Text = bsObj.h1
    articles = bsObj.findAll("a")
    for i in articles:
        articleUrl = i["href"]
        result = checkUrl(articleUrl)
        if result == True:
            if i.h3 is not None:
                if checkTitle(i.h3.get_text()) is True:
                    siteTitleJa = fetch.translate_text('ja', i.h3.get_text())
                    siteTitleRaw = i.h3.get_text()
                    bodyTextJa = fetch.translate_text('ja', i.get_text())
                    bodyTextRaw = i.get_text()
                    print(siteTitleJa)
                    print(bodyTextJa)
                    # def insertWrap(conn, urlMD5, url, siteLogoUrl, articleImageUrl, siteTitleJa, siteTitleRaw, bodyTextJa, bodyTextRaw, langCode):
                    articleImageUrl = 'https://cdn-images-1.medium.com/max/1600/1*gGXtUAqvryrBRkxNvodSzA.png'
                    insertWrap(conn, makeHash(articleUrl), articleUrl, articleImageUrl, articleImageUrl, siteTitleJa, siteTitleRaw,
                               bodyTextJa, bodyTextRaw, 'en')





                    # params1 = bsObj.findAll("h1")
                    # params2 = bsObj.findAll("div", {"class": "excerpt entry-summary"})
                    # params3 = bsObj.findAll("picture")
                    #
                    # head = []
                    # for h in params1:
                    #     head.append(h.text)
                    #
                    # summary = []
                    # for para2 in params2:
                    #     summary.append(para2.p.text)
                    #
                    # pic = []
                    # for obj in params3:
                    #     list = obj.findAll("source",{"media": "--small"})
                    #     for l in list:
                    #         #print(l)
                    #         hoge = l["data-srcset"]
                    #         pic.append(hoge)
                    #
                    # print(len(head))
                    # print(len(summary))
                    # print(len(pic))
                    #
                    # host = getHost(url)
                    # icon = 'http://ch.res.nimg.jp/img/system/blog_author/ch901.jpg'
                    #
                    # num = 0
                    # for i in head:
                    #     title = translate_text('ja', head[num])
                    #     bodyEn = summary[num]
                    #     bodyJa = translate_text('ja', bodyEn)
                    #     imgUrl = pic[num]
                    #     mydb.insert(conn, 'id' + str(time.time()), url, host, imgUrl, title, imgUrl, bodyEn, bodyJa)
                    #     num += 1
                    #
                    # #title = translate_text('ja', cleanhtml(bsObj.title))


# main
conn = mydb.connect()
url = 'https://medium.com/tag/programming/latest'
fetchMedium(conn, url)
