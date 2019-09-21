

# -*- coding: utf-8 -*-


import re
from bs4 import BeautifulSoup4


PageUrl="https://www.lixinger.com/analytics/company/sz/300383/detail/announcement?announcement-type=fs&page-index=0"

file_url = re.search('http://file.finance.sina.com.cn/211.154.219.97:9494/.*?PDF',PageUrl)