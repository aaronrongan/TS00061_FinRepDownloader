

# -*- coding: utf-8 -*-

#读取html文件
# 从新浪财经获取PDF
import re
import requests
from bs4 import BeautifulSoup
import lxml

headers1={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:55.0) Gecko/20100101 Firefox/55.0"}
send_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",    "Connection": "keep-alive",    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",    "Accept-Language": "zh-CN,zh;q=0.8"    }

r = requests.get('http://vip.stock.finance.sina.com.cn/corp/go.php/vCB_Bulletin/stockid/002271/page_type/ndbg.phtml',timeout=10,headers=send_headers)
r.encoding='gbk'
r.close()

# print(r.text)

soup=BeautifulSoup(r.text,'lxml')

# print(soup.prettify())
# print(r.headers)

# print(r.json())

# print(soup.findall('div',class_="datelist").a.text)
datelist=soup.find_all('div',class_="datelist")

#得到如下内容
#

# for eachdate in datelist.find('a'):
#     print(eachdate.text)

# for each in soup.find('div',class_="datelist")
#PageUrl="https://www.lixinger.com/analytics/company/sz/300383/detail/announcement?announcement-type=fs&page-index=0"

#file_url = re.search('http://file.finance.sina.com.cn/211.154.219.97:9494/.*?PDF',PageUrl)