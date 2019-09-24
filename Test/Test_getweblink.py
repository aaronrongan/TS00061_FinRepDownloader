

# -*- coding: utf-8 -*-

#读取html文件

import re
import requests
from bs4 import BeautifulSoup

headers1={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:55.0) Gecko/20100101 Firefox/55.0"}
r = requests.get('https://www.lixinger.com/analytics/company/sz/300383/detail/announcement?announcement-type=fs&page-index=0',timeout=10,headers=headers1)

print(r.encoding)

soup=BeautifulSoup(r,'lxml')

print(soup.prettify())
# print(r.headers)

# print(r.json())

#PageUrl="https://www.lixinger.com/analytics/company/sz/300383/detail/announcement?announcement-type=fs&page-index=0"

#file_url = re.search('http://file.finance.sina.com.cn/211.154.219.97:9494/.*?PDF',PageUrl)