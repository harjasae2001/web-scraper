import requests


proxies = {
    'http': 'http://brd-customer-hl_7e1496e5-zone-residential_proxy2:by37c8ur2lkb@brd.superproxy.io:22225',
     'https': 'http://brd-customer-hl_7e1496e5-zone-residential_proxy2:by37c8ur2lkb@brd.superproxy.io:22225',

            }

r = requests.get('https://api64.ipify.org?format=json', proxies=proxies)
print(r.json())
