

# -*- coding: utf-8 -*-


import re
import requests
# from bs4 import beautifulsoup4

r = requests.get('https://www.lixinger.com/analytics/company/sz/300383/detail/announcement?announcement-type=fs&page-index=0')

# print(r.encoding)

# print(r.headers)

# print(r.json())

#PageUrl="https://www.lixinger.com/analytics/company/sz/300383/detail/announcement?announcement-type=fs&page-index=0"

#file_url = re.search('http://file.finance.sina.com.cn/211.154.219.97:9494/.*?PDF',PageUrl)