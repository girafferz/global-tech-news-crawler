from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from google.cloud import translate
import six

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

    print(u'Text: {}'.format(result['input']))
    print(u': {}'.format(result['translatedText']))
    #print(u'Detected source language: {}'.format(
    #    result['detectedSourceLanguage']))


html = urlopen("https://www.quora.com/Is-Node-js-a-better-choice-than-Python-for-server-side-development-i-e-why-would-one-use-Python-over-Javascript-and-Node-js")
bsObj = BeautifulSoup(html.read(), "html.parser")
#print(cleanhtml(bsObj.title))
translate_text('ja', cleanhtml(bsObj.title))

paras = bsObj.findAll("p", {"class":"qtext_para"})
for hoge in paras:
    if makeSentence(hoge) != '':
        print('-------')
        raw = makeSentence(hoge)
        #print(raw)
        translate_text('ja', raw)
