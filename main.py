import requests
from lxml import etree

URL="http://youdao.com/w/eng/"

test=URL+"enchant"
req=requests.Session()

req.get(test)

