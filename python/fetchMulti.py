# coding=utf-8
# -*- coding: utf-8 -*-
import io
import sys, codecs
from time import sleep

#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import mydb, fetch
import numpy
from yelp_uri.encoding import recode_uri

from urllib.error import HTTPError
from urllib.error import URLError

print('start')
conn = mydb.connect()
print('db connect')

host = 'https://www.quora.com'
target = '/What-are-the-biggest-websites-built-with-Node-js-on-the-server-side'
for num in range(0,10000):
    try:
        print(num)
        sleep(1)
        print('--fetchMulti 26--')
        ht = host + str(target)
        print('--fetchMulti 27--')
        ht = recode_uri(ht)
        print('--fetchMulti 28--')
        hrefs = fetch.getQuoraUrls(conn, ht)
        prev = hrefs
        if (len(hrefs) > 0):
            prev = hrefs

        print('--fetchMulti 29--')
        target = recode_uri(numpy.random.choice(prev))
        print('--fetchMulti 30--')
        ht = host + target
        print('--fetchMulti 31--')
        fetch.fetchQuora(conn, ht)
        print(ht)
    except HTTPError as e:
        print(e)
    except URLError as e:
        print("The server could not be found!")
    else:
        print("It Worked!")


#fetch.fetchLifeHacker(conn, 'https://lifehacker.com/tag/programming')
