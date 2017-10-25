# coding=utf-8
# -*- coding: utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import fetch

import mydb

conn = mydb.connect()

fetch.fetchQuora(conn, 'https://www.quora.com/Is-Node-js-a-better-choice-than-Python-for-server-side-development-i-e-why-would-one-use-Python-over-Javascript-and-Node-js')
fetch.fetchLifeHacker(conn, 'https://lifehacker.com/tag/programming')
