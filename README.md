# dependency
```
pip install -U setuptools
pip install wheel
pip install mysql-connector-python-rf
pip install six
pip install beautifulsoup4
pip install --upgrade google-cloud
pip install numpy
pip install yelp_uri
```
# proxy with ua
```
#!/usr/bin/env python
import urllib.request
PROXIES = {
            'http' : 'http://13.112.243.246:60089'
            }
proxy_handler = urllib.request.ProxyHandler(PROXIES)
opener = urllib.request.build_opener(proxy_handler)
headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0"}
url = 'http://www.ugtop.com/spill.shtml'
req = urllib.request.Request(url,None,headers)
data = opener.open(req).read()
print(data.decode('utf-8'))
```
