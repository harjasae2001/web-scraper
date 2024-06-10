import requests
from bs4 import BeautifulSoup
import urllib.request
opener = urllib.request.build_opener(
urllib.request.ProxyHandler(
            {'http': 'http://brd-customer-hl_7e1496e5-zone-residential_proxy2:by37c8ur2lkb@brd.superproxy.io:22225',
            'https': 'http://brd-customer-hl_7e1496e5-zone-residential_proxy2:by37c8ur2lkb@brd.superproxy.io:22225'}))

url = 'https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=iphone&crid=1ELE5U2TRNHKI&sprefix=ipho%2Caps%2C346'
r = opener.open(url).text()


# r = requests.get(url, proxies = proxies)
# with open("sample.html", "r") as f:
#     html_doc = f.read()

soup = BeautifulSoup(r, 'html.parser')
print(soup.prettify())