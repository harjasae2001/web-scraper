# #!/usr/bin/env python
# print('If you get error "ImportError: No module named \'six\'" install six:\n'+\
#     '$ sudo pip install six');
# print('To enable your free eval account and get CUSTOMER, YOURZONE and ' + \
#     'YOURPASS, please contact sales@brightdata.com')

import urllib.request
opener = urllib.request.build_opener(
urllib.request.ProxyHandler(
            {'http': 'http://brd-customer-hl_7e1496e5-zone-residential_proxy2:by37c8ur2lkb@brd.superproxy.io:22225',
            'https': 'http://brd-customer-hl_7e1496e5-zone-residential_proxy2:by37c8ur2lkb@brd.superproxy.io:22225'}))
print(opener.open('http://lumtest.com/myip.json').read())