# coding=utf-8
# -*- coding: utf-8 -*-
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import mydb, fetch

print('start')
conn = mydb.connect()
print('db connect')

fetch.fetchQuora(conn, 'https://www.quora.com/Is-Node-js-a-better-choice-than-Python-for-server-side-development-i-e-why-would-one-use-Python-over-Javascript-and-Node-js')
#fetch.fetchLifeHacker(conn, 'https://lifehacker.com/tag/programming')
