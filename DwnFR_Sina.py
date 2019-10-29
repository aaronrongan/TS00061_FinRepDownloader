#目的:从新浪财经获取PDF

#191026 更新
#使用命令行独立执行方式，用户输入年份、代码，已有的重复文件不要覆盖, 打包成一个独立文件ts0061


import re
import requests
from bs4 import BeautifulSoup
import lxml
import urllib
import os
import csv

from setting import filename_ar, filename_q2, filename_q1, filename_q3, filename_zhaogu, \
    downloadpath1, url_ar_1, url_ar_2, \
    url_q1_1, url_q1_2, url_q2_1, url_q2_2, \
    url_q3_1, url_q3_2, \
    url_zhaogu_1, url_zhaogu_2

from setting import msg1, msg2, msg3

#参数说明
#   codenumber = '002271'
#   downloadtype = ’4‘  # 4-年报；1-1季报；2-中报；3-3季报；5-招股; 0-4个季度报表全部下载
#   downloadflag = True  # True为实际下载，False为不下载
#   debugflag = False  # True为输出调试信息，False为不输出
#   yeartype 年度, 为’0‘则下载所有报表 #

def DownloadFR(downloadtype,yeartype,codenumber,downloadflag,debugflag):

    headers1 = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:55.0) Gecko/20100101 Firefox/55.0"}
    send_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "Connection": "keep-alive",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8"}

    if downloadtype == '4':
        realurl = url_ar_1 + codenumber + url_ar_2
        filetypestr = filename_ar
    elif downloadtype == '1':
        realurl = url_q1_1 + codenumber + url_q1_2
        filetypestr = filename_q1
    elif downloadtype == '2':
        realurl = url_q2_1 + codenumber + url_q2_2
        filetypestr = filename_q2
    elif downloadtype == '3':
        realurl = url_q3_1 + codenumber + url_q3_2
        filetypestr = filename_q3
    elif downloadtype == '5':
        realurl = url_zhaogu_1 + codenumber + url_zhaogu_2
        filetypestr = filename_zhaogu
    else:
        realurl = url_ar_1 + codenumber + url_ar_2
        filetypestr = filename_ar

    if debugflag == True:
        print(realurl)

    r = requests.get(realurl, timeout=10, headers=send_headers)
    r.encoding = 'gbk'
    r.close()
    if debugflag==True:
        print(r)

    soup = BeautifulSoup(r.text, 'lxml')

    # regex_str=
    # print(soup.prettify())

    # 关键代码
    #找到显示的各年度
    try:
        datelist = soup.find('div', class_="datelist").find_all('a')  # 不是用find_all("href")
    except:
        print("未找到地址。年度："+ yeartype + "；代码：" + codenumber)
        return

   # global yearnumber
    # ########################读取代码和名称的字典文件,包括所有代码在内,用Full.csv
    with open('./StockList_Full.csv', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file, fieldnames=['code', 'name'])
        dict = {}
        for row in csv_reader:
            dict[row['code']] = row['name']
        if dict[codenumber]!="":
            if debugflag == True:
                print(dict[codenumber])
            else:
                print(msg3)
    csv_file.close()

    #分析每年，eachaddress为单年年份
    for eachaddress in datelist:
        try:
            yearnumber='0'
            if debugflag == True:
                print(eachaddress.text)
            # yearnumber=re.search(r"(2[]+年)",eachaddress.text)
            if downloadtype == '1' or downloadtype == '2' or downloadtype == '3' or downloadtype == '4':
                yearnumber = re.search(r'(\d{4})', eachaddress.text)
                if debugflag == True:
                    #print("yearnumber" + yearnumber.group(1))
                    print("yearnumber" + yearnumber.group(0))
            elif downloadtype == '5':
                yearnumber = '招股说明书'
        except AttributeError as e:
            print("except: 未找到链接地址。代码:" + dict[codenumber])
            break

        #当输入年份为0时，需要所有的年份，
        #当输入年份不为0而且和找到的年份不相同时，则跳过
        #try:
        if yeartype!= yearnumber.group(0) and yeartype !='0':
        # BUG：yeartype1为0时，无法下载
        # 原因：yeartype!="0" 应该是!=0，包括downloadtype的字符串也是容易混淆成数字
            if debugflag==True:
                print("jump out")
            continue
        #需要单独某年
        else:
            if debugflag == True:
                print(eachaddress.text + ':' + 'http://vip.stock.finance.sina.com.cn/' + eachaddress.get('href'))

            PDFWebpage = 'http://vip.stock.finance.sina.com.cn/' + eachaddress.get('href')

            if debugflag == True:
                print(filetypestr)

            # 招股说明书无法在新浪这个网站下载PDF，也许只能下载HTML格式文件
            if downloadtype == '1' or downloadtype == '2' or downloadtype == '3' or downloadtype == '4':
                r = requests.get(PDFWebpage, timeout=10, headers=send_headers)
                r.encoding = 'gbk'
                r.close()

                soup = BeautifulSoup(r.text, 'lxml')
                #print(soup.text)
                try:
                    PDFAddress = soup.find('table', id="allbulletin").find('a').get('href')
                    if debugflag == True:
                        print(PDFAddress)
                    filename = os.path.basename(PDFAddress)
                    downloadpath2 = downloadpath1 + codenumber + ' ' + dict[codenumber] + '//'

                    if debugflag == True:
                        print(downloadpath2)
                    # filepathname='../../../' + codenumber + '_' +dict[codenumber] +'_' + yearnumber.group(0) + filetypestr + '.pdf' #+ filename
                    filepathname = downloadpath2 + codenumber + '_' + dict[codenumber] + '_' + yearnumber.group(
                        0) + filetypestr + '.pdf'  # + filename

                    if debugflag == True:
                        print(filepathname)

                    # 判断该文件是否存在
                    if os.path.exists(filepathname):
                        print(codenumber + '的' + yearnumber.group(0) + "年第" + downloadtype +"季度文件已存在!")
                    else:
                        if downloadflag == True:
                            #此处条件夹文件
                            #print("准备下载" + PDFAddress)
                            try:
                                urllib.request.urlretrieve(PDFAddress, filename=filepathname)
                                print("已下载" + PDFAddress)
                            except:
                                print("下载地址有误，无法下载")
                except AttributeError as e:
                    print("except: 未找到PDF链接地址" )
        #except:#
            #print("attribute 错误")

