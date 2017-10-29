# coding=utf-8
# -*- coding: utf-8 -*-
import io
import sys
from time import sleep

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import mydb, fetch

print('start')
conn = mydb.connect()
print('db connect')

#fetch.fetchQuora(conn, 'https://www.quora.com/Is-Node-js-a-better-choice-than-Python-for-server-side-development-i-e-why-would-one-use-Python-over-Javascript-and-Node-js')

baseUrls = ['https://www.quora.com/How-does-Mark-Zuckerberg-actually-make-money',
      'https://www.quora.com/Is-Python-a-dying-language-A-friend-of-my-grandmother%E2%80%99s-is-a-computer-scientist-from-MIT-He-told-me-that-I-should-not-learn-Python-because-its-a-dying-language-and-that-I-should-learn-Assembly-because-its-better-than-Python',
            ]

for u in baseUrls:
    sleep(3)
    print(u)
    hrefs = fetch.getQuoraUrls(conn, u)
    print(hrefs)
    for href in hrefs:
        print(href)
        sleep(3)
        target = 'https://www.quora.com/' + href
        fetch.fetchQuora(conn, target)

#fetch.fetchLifeHacker(conn, 'https://lifehacker.com/tag/programming')
