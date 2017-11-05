from urllib.parse import urlparse
import mysql.connector
import os


def connect():
    hoge = os.environ["MYSQL_PASS"]
    mysql_url = os.environ["MYSQL_URL"]
    mysql_user = os.environ["MYSQL_USER"]
    url = urlparse('mysql://' + mysql_user + ':' + hoge + '@' + mysql_url + ':3306/news')

    conn = mysql.connector.connect(
            host = url.hostname or 'localhost',
            port = url.port or 3306,
            user = url.username or 'root',
            password = url.password or hoge,
            database = url.path[1:],
            )

    return conn


def insert(conn, urlMD5, url, siteLogoUrl, articleImageUrl, siteTitleJa, siteTitleRaw, bodyTextJa, bodyTextRaw, langCode):
    try:
        cur = conn.cursor()
        print(u'urlMD5: ' + urlMD5.encode('utf-8'))
        print(u'url: ' + url.encode('utf-8'))
        print(u'siteLogoUrl: ' + siteLogoUrl.encode('utf-8'))
        print(u'articleImageUrl: ' + articleImageUrl.encode('utf-8'))
        print(u'siteTitleJa: ' + siteTitleJa.encode('utf-8'))
        print(u'siteTitleRaw: ' + siteTitleRaw.encode('utf-8'))
        print(u'bodyTextJa: ' + bodyTextJa.encode('utf-8'))
        print(u'bodyTextRaw: ' + bodyTextRaw.encode('utf-8'))
        print(u'langCode: ' + langCode.encode('utf-8'))

        cur.execute('INSERT INTO article (urlMD5, url, siteLogoUrl, articleImageUrl, siteTitleJa, ' + \
                    'siteTitleRaw, bodyTextJa, bodyTextRaw, langCode) ' + \
                    'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)', \
            [urlMD5, url, siteLogoUrl, articleImageUrl, siteTitleJa, siteTitleRaw, bodyTextJa, bodyTextRaw, langCode])
        conn.commit()
        print('----conn.commit()----')

    except UnicodeEncodeError as e:
        print('1--exception--UnicodeEncodeError---')
        print(e)
        print('2--exception--UnicodeEncodeError---')
        conn.rollback()

    except:
        print('exception-----')
        conn.rollback()
