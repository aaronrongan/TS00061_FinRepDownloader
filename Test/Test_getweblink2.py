

# -*- coding: utf-8 -*-

#读取html文件
# 从新浪财经获取PDF
import re
import requests
from bs4 import BeautifulSoup
import lxml
import urllib
import os

headers1={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:55.0) Gecko/20100101 Firefox/55.0"}
send_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",    "Connection": "keep-alive",    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",    "Accept-Language": "zh-CN,zh;q=0.8"    }

r = requests.get('http://vip.stock.finance.sina.com.cn/corp/go.php/vCB_Bulletin/stockid/002271/page_type/ndbg.phtml',timeout=10,headers=send_headers)
r.encoding='gbk'
r.close()

# print(r.text)

soup=BeautifulSoup(r.text,'lxml')

# print(soup.prettify())

#关键代码
datelist=soup.find('div',class_="datelist").find_all('a') #不是用find_all("href")

for eachaddress in datelist:
    # print(eachaddress.text + ':' + 'http://vip.stock.finance.sina.com.cn/' + eachaddress.get('href'))
    PDFWebpage='http://vip.stock.finance.sina.com.cn/' + eachaddress.get('href')

    r = requests.get(PDFWebpage, timeout=10, headers=send_headers)
    r.encoding = 'gbk'
    r.close()

    soup = BeautifulSoup(r.text, 'lxml')

    PDFAddress=soup.find('table',id="allbulletin").find('a').get('href')
    print(PDFAddress)
    filename=os.path.basename(PDFAddress)
    filename='../../../' + filename
    print(filename)
    # urllib.request.urlretrieve(PDFAddress, filename=filename)

#得到如下内容，从中提取href文本
# http://vip.stock.finance.sina.com.cn/corp/view +以下内容
#[<div class="datelist">
#      <ul>
# 			2019-03-28 <a href="/corp/view/vCB_AllBulletinDetail.php?stockid=002271&amp;id=5118961" target="_blank">东方雨虹：2018年年度报告</a><br/>
# 			2018-04-24 <a href="/corp/view/vCB_AllBulletinDetail.php?stockid=002271&amp;id=4309197" target="_blank">东方雨虹：2017年年度报告</a><br/>
# 			2017-04-21 <a href="/corp/view/vCB_AllBulletinDetail.php?stockid=002271&amp;id=3265799" target="_blank">东方雨虹：2016年年度报告</a><br/>
# 			2016-04-23 <a href="/corp/view/vCB_AllBulletinDetail.php?stockid=002271&amp;id=2394374" target="_blank">东方雨虹：2015年年度报告</a><br/>
# 			2015-04-28 <a href="/corp/view/vCB_AllBulletinDetail.php?stockid=002271&amp;id=1754542" target="_blank">北京东方雨虹防水技术股份有限公司2014年年度报告</a><br/>
# 			2014-03-18 <a href="/corp/view/vCB_AllBulletinDetail.php?stockid=002271&amp;id=1319510" target="_blank">北京东方雨虹防水技术股份有限公司2013年年度报告</a><br/>
# 			2013-04-13 <a href="/corp/view/vCB_AllBulletinDetail.php?stockid=002271&amp;id=1090780" target="_blank">北京东方雨虹防水技术股份有限公司2012年年度报告</a><br/>
# 			2012-04-13 <a href="/corp/view/vCB_AllBulletinDetail.php?stockid=002271&amp;id=881574" target="_blank">北京东方雨虹防水技术股份有限公司2011年年度报告</a><br/>
# 			2011-04-23 <a href="/corp/view/vCB_AllBulletinDetail.php?stockid=002271&amp;id=708836" target="_blank">北京东方雨虹防水技术股份有限公司2010年年度报告</a><br/>
# 			2010-01-30 <a href="/corp/view/vCB_AllBulletinDetail.php?stockid=002271&amp;id=504805" target="_blank">北京东方雨虹防水技术股份有限公司2009年年度报告</a><br/>
# 	    </ul>
# </div>]

# for eachdate in datelist.find('a'):
#     print(eachdate)

# for each in soup.find('div',class_="datelist")
#PageUrl="https://www.lixinger.com/analytics/company/sz/300383/detail/announcement?announcement-type=fs&page-index=0"

#file_url = re.search('http://file.finance.sina.com.cn/211.154.219.97:9494/.*?PDF',PageUrl)