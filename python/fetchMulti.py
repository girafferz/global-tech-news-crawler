# coding=utf-8
# -*- coding: utf-8 -*-
import io
import sys, codecs
from time import sleep

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import mydb, fetch
import numpy
from yelp_uri.encoding import recode_uri

print('start')
conn = mydb.connect()
print('db connect')

#fetch.fetchQuora(conn, 'https://www.quora.com/Is-Node-js-a-better-choice-than-Python-for-server-side-development-i-e-why-would-one-use-Python-over-Javascript-and-Node-js')

baseUrls = ['https://www.quora.com/How-does-Mark-Zuckerberg-actually-make-money',
            'https://www.quora.com/Is-Python-a-dying-language-A-friend-of-my-grandmother%E2%80%99s-is-a-computer-scientist-from-MIT-He-told-me-that-I-should-not-learn-Python-because-its-a-dying-language-and-that-I-should-learn-Assembly-because-its-better-than-Python',
            'https://www.quora.com/What-are-some-cool-Python-tricks',
            'https://www.quora.com/Which-is-better-Java-or-Python-And-how',
            'https://www.quora.com/Which-is-the-best-book-for-learning-python-for-absolute-beginners-on-their-own',
            'https://www.quora.com/Between-Java-and-Python-which-one-is-better-to-learn-first-and-why',
            'https://www.quora.com/What-are-some-interesting-things-to-do-with-Python-I-want-to-make-something-related-to-big-data-or-machine-learning',
            'https://www.quora.com/Which-is-better-PHP-or-Python-Why',
            'https://www.quora.com/What-is-Python-primarily-used-for',
            'https://www.quora.com/How-should-I-start-learning-Python-1',
            'https://www.quora.com/Which-is-better-Java-or-Python-And-how',
            'https://www.quora.com/What-is-Python-primarily-used-for',
            'https://www.quora.com/What-is-Node-js-for-Are-there-some-good-getting-started-with-Node-js-tutorials-which-you-can-recommend',
            'https://www.quora.com/What-is-Python-primarily-used-for',
            'https://www.quora.com/How-good-is-Node-js',
            'https://www.quora.com/Should-I-learn-Node-js-or-Ruby-on-Rails'
            ]

# for u in baseUrls:
#     sleep(3)
#     print(u)
#     hrefs = fetch.getQuoraUrls(conn, u)
#     print(hrefs)
#     for href in hrefs:
#         print(href)
#         sleep(3)
#         target = 'https://www.quora.com/' + href
#         fetch.fetchQuora(conn, target)

host = 'https://www.quora.com'
target = '/Why-would-I-use-React-over-AngularJS'
for num in range(0,10000):
    print(num)
    sleep(10)
    target = recode_uri(host + str(target))
    hrefs = fetch.getQuoraUrls(conn, recode_uri(host + str(target)))
    target = recode_uri(numpy.random.choice(hrefs))
    fetch.fetchQuora(conn, host + str(target))
    print(host + str(target))

#fetch.fetchLifeHacker(conn, 'https://lifehacker.com/tag/programming')
