# coding=utf-8
# -*- coding: utf-8 -*-

from time import sleep
import re
import time
from urllib.parse import urlparse
from urllib.request import urlopen

import six
from bs4 import BeautifulSoup
from google.cloud import translate

import mydb
import hashlib
import pretty
from yelp_uri.encoding import recode_uri


def makeSentence(raw_html):
    return lengthCheck(cleanhtml(raw_html))

def lengthCheck(sentence):
    if len(sentence) < 10 :
        return ''
    else:
        return sentence

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', str(raw_html))
    return cleantext

def translate_text(target, text):
    """Translates text into the target language.
    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(
        text, target_language=target)

    #print(u'Text: {}'.format(result['input']))
    #print(u': {}'.format(result['translatedText']))
    #print(u'Detected source language: {}'.format(
    #    result['detectedSourceLanguage']))
    return result['translatedText']

def checkTitle(title):
    check = False
    if re.search(r"Node", title):
        print('--58--')
        check = True
    if re.search(r"JavaScript", title):
        print('--61--')
        check = True
    if re.search(r"JS", title):
        print('--64--')
        check = True
    if re.search(r"React", title):
        print('--67--')
        check = True
    if re.search(r"Python", title):
        print('--70--')
        check = True
    if re.search(r"python", title):
        print('--73--')
        check = True
    print('--title check--')
    print(check)
    return check

def fetchQuora(conn, url):
    a = hashlib.md5()
    a.update(url.encode('utf-8'))
    urlMD5 = hashlib.md5(url.encode('utf8')).hexdigest()

    print('---fetchQuora---')
    print(recode_uri(str(url)))
    print(urlMD5)
    sleep(1)
    html = urlopen(recode_uri(str(url)))
    bsObj = BeautifulSoup(str(html.read()), "html.parser")
    #title = ''
    #params1 = bsObj.findAll("span", {"class":"rendered_qtext"})
    #params1 = bsObj.findAll("div", {"class":"inline_editor_content"})

    if (checkTitle(recode_uri(cleanhtml(bsObj.title)))):
        return False

    title = translate_text('ja', cleanhtml(bsObj.title))
    params1 = bsObj.findAll("p", {"class":"qtext_para"})

    print('--params1--')
    print(len(params1))

    bodyJa = []
    bodyEn = []

    for hoge in params1:
        if makeSentence(str(hoge)) != '':
            raw = makeSentence(hoge)
            bodyJa.append(translate_text('ja', raw))
            bodyEn.append(raw)

    siteLogoUrl = 'https://qsf.ec.quoracdn.net/-3-images.logo.wordmark_default.svg-26-32753849bf197b54.svg'
    articleImageUrl = 'https://qsf.ec.quoracdn.net/-3-images.logo.wordmark_default.svg-26-32753849bf197b54.svg'
    siteTitleJa =  title
    siteTitleRaw = cleanhtml(bsObj.title)
    bodyTextJa = "\n".join(bodyJa)
    bodyTextRaw = "\n".join(bodyEn)
    langCode = 'en'

    siteTitleJa = pretty.bodyTextJa(siteTitleJa)
    bodyTextJa = pretty.bodyTextJa(bodyTextJa)

    mydb.insert(conn, urlMD5, url, siteLogoUrl, articleImageUrl, siteTitleJa, siteTitleRaw, bodyTextJa, bodyTextRaw, langCode)

def getQuoraUrls(conn, url):
    sleep(1)
    html = urlopen(url);
    bsObj = BeautifulSoup(html.read(), "html.parser");
    params1 = bsObj.findAll("a", {"class":"question_link"})
    #print(params1[0].get('href'))
    hrefs = []
    for i in params1:
        hrefs.append(i.get('href'))
    return hrefs

def fetchLifeHacker(conn, url):
    html = urlopen(url)
    bsObj = BeautifulSoup(html.read(), "html.parser")
    params1 = bsObj.findAll("h1", {"class": "headline"})
    params2 = bsObj.findAll("div", {"class": "excerpt entry-summary"})
    params3 = bsObj.findAll("picture")

    head = []
    for h in params1:
        head.append(h.text)

    summary = []
    for para2 in params2:
        summary.append(para2.p.text)

    pic = []
    for obj in params3:
        list = obj.findAll("source",{"media": "--small"})
        for l in list:
            #print(l)
            hoge = l["data-srcset"]
            pic.append(hoge)

    print(len(head))
    print(len(summary))
    print(len(pic))

    host = getHost(url)
    icon = 'http://ch.res.nimg.jp/img/system/blog_author/ch901.jpg'

    num = 0
    for i in head:
        title = translate_text('ja', head[num])
        bodyEn = summary[num]
        bodyJa = translate_text('ja', bodyEn)
        imgUrl = pic[num]
        mydb.insert(conn, 'id' + str(time.time()), url, host, imgUrl, title, imgUrl, bodyEn, bodyJa)
        num += 1

    #title = translate_text('ja', cleanhtml(bsObj.title))
