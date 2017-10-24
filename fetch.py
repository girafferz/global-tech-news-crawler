# coding=utf-8
# -*- coding: utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from google.cloud import translate
import six

import mydb
import time

conn = mydb.connect()

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


url = 'https://www.quora.com/Is-Node-js-a-better-choice-than-Python-for-server-side-development-i-e-why-would-one-use-Python-over-Javascript-and-Node-js'
html = urlopen(url)
bsObj = BeautifulSoup(html.read(), "html.parser")
title = translate_text('ja', cleanhtml(bsObj.title))
params1 = bsObj.findAll("p", {"class":"qtext_para"})

body = []
for hoge in params1:
    if makeSentence(hoge) != '':
        raw = makeSentence(hoge)
        body.append(translate_text('ja', raw))

print('--body--')
print("\n".join(body))

#mydb.insert(conn, 'idhash' + str(time.time()), url, 'www.quora.com', 'https://qsf.ec.quoracdn.net/-3-images.logo.wordmark_default.svg-26-32753849bf197b54.svg', title, 'https://qsf.ec.quoracdn.net/-3-images.logo.wordmark_default.svg-26-32753849bf197b54.svg', "\n".join(body)) 


