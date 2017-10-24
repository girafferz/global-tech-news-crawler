import mydb
import time

conn = mydb.connect()

mydb.insert(conn, \
'idhash2' + str(time.time()), \
'https://www.quora.com/Should-I-learn-Node-js-or-Python', \
'www.quora.com', \
'https://qsf.ec.quoracdn.net/-3-images.logo.wordmark_default.svg-26-32753849bf197b54.svg', \
'Should I learn Node js or Python?', \
'https://qsf.ec.quoracdn.net/-3-images.logo.wordmark_default.svg-26-32753849bf197b54.svg', \
'Node.js is a better choice if your focus is on web applications and web site development.')
