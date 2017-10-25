# coding=utf-8
# -*- coding: utf-8 -*-
import sys
import io

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from google.cloud import translate
import six
import time
import mydb
from urllib.parse import urlparse

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

def fetchQuora(conn, url):
    #url = 'https://www.quora.com/Is-Node-js-a-better-choice-than-Python-for-server-side-development-i-e-why-would-one-use-Python-over-Javascript-and-Node-js'
    print('---url---')
    print(url)
    html = urlopen(url)
    bsObj = BeautifulSoup(html.read(), "html.parser")
    title = translate_text('ja', cleanhtml(bsObj.title))
    #params1 = bsObj.findAll("p", {"class":"qtext_para"})
    params1 = bsObj.findAll("span", {"class":"rendered_qtext"})

    print('--params1--')
    print(params1)

    bodyJa = []
    bodyEn = []

    for hoge in params1:
        if makeSentence(hoge) != '':
            raw = makeSentence(hoge)
            bodyJa.append(translate_text('ja', raw))
            bodyEn.append(raw)

    print('--bodyEn--')
    print("\n".join(bodyEn))
    print('--bodyJa--')
    print("\n".join(bodyJa))

    mydb.insert(conn, 'id' + str(time.time()), url, 'www.quora.com', 'https://qsf.ec.quoracdn.net/-3-images.logo.wordmark_default.svg-26-32753849bf197b54.svg', title, 'https://qsf.ec.quoracdn.net/-3-images.logo.wordmark_default.svg-26-32753849bf197b54.svg', "\n".join(bodyEn), "\n".join(bodyJa))

def getHost(url):
    url = urlparse(url)
    host = url.hostname or 'localhost'
    print(host)
    return host

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
