from urllib.parse import urlparse
import mysql.connector
import os

def connect():
    hoge = os.environ["HOGE"]
    url = urlparse('mysql://root:' + hoge + '@localhost:3306/news')

    conn = mysql.connector.connect(
            host = url.hostname or 'localhost',
            port = url.port or 3306,
            user = url.username or 'root',
            password = url.password or hoge,
            database = url.path[1:],
            )

    return conn

def insert(conn, id, originUrl, originCaption, imageUrl, title, iconImageUrl, h1):
    try:
        cur = conn.cursor()
        cur.execute('INSERT INTO article (id, originUrl, originCaption, imageUrl, title, iconImageUrl, h1 ) VALUES (%s, %s, %s, %s, %s, %s, %s)', \
            [id, originUrl, originCaption, imageUrl, title, iconImageUrl, h1])
        conn.commit()
    except:
        print('exception-----')
        conn.rollback()
        raise



