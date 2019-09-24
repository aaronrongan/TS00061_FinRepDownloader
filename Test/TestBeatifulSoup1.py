# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests

headers1={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:55.0) Gecko/20100101 Firefox/55.0"}
r = requests.get('https://www.lixinger.com/analytics/company/sz/300383/detail/announcement?announcement-type=fs&page-index=0',timeout=10,headers=headers1).text

source=requests.get('https://www.lixinger.com/analytics/company/sz/300383/detail/announcement?announcement-type=fs&page-index=0').text

# source=requests.get('http://vip.stock.finance.sina.com.cn/corp/go.php/vCB_Bulletin/stockid/002271/page_type/ndbg.phtml').text


soup=BeautifulSoup(r,'lxml')

print(soup)









