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
# proxy
```
#!/usr/bin/env python
import urllib.request

PROXIES = {
            'http' : 'http://{PROXT_HOST}:{PROXY_PORT}'
            }
proxy_handler = urllib.request.ProxyHandler(PROXIES)
opener = urllib.request.build_opener(proxy_handler)
data = opener.open('http://www.ugtop.com/spill.shtml').read()
print(data.decode('utf-8'))
```
