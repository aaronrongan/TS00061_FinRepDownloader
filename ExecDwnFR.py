
#主执行文件
import csv
import os
from DwnFR_Sina import DownloadFR


codelist=[]

codenumber=str(input('输入代码：0-根据StockList.csv; 其它-根据实际代码:;[0]'))
if codenumber=='':
    codenumber='0'
yeartype1=str(input('输入年份: 0-所有年；其它-实际年份;[0]:'))
if yeartype1=='':
    yeartype1='0'
downloadtype1=str(input('输入年报类型：0-所有财报; 1-一季报；2-中报；3-三季报;4-年报；[0]:'))
if downloadtype1=='':
    downloadtype1='0'
downloadflag1=str(input('是否下载还是仅仅测试而不下载:0-不下载;1-下载;[1]'))
if downloadflag1=='1' or downloadflag1=='':
    downloadflag1=True
else:
    downloadflag1 = False
verboseflag=str(input('是否输出中间信息：1-输出调试信息；0-不输出调试信息;[1]:'))
if verboseflag=='1' or verboseflag=='':
    verboseflag=True
else:
    verboseflag = False

#os.path.dirname(os.path.abspath('.'))

if codenumber =='0' :
    with open('./StockList.csv',newline='') as csv_file:
        # with open('StockList.csv',newline='', encoding = 'UTF-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            # print(row['code'],row['name'])
            # codelist.append(row['code'])
            if downloadtype1 == '0':
                for each in range(1, 5):
                    DownloadFR(str(each), yeartype=yeartype1, codenumber=row['code'], downloadflag=downloadflag1,
                               debugflag=verboseflag)
            else:
                DownloadFR(downloadtype1, yeartype=yeartype1, codenumber=row['code'], downloadflag=downloadflag1,
                           debugflag=verboseflag)
    csv_file.close()
else:
    #下载4个季度财报,循环
    if downloadtype1=='0':
        for each in range(1, 5):
            DownloadFR(str(each), yeartype=yeartype1, codenumber=codenumber, downloadflag=downloadflag1, debugflag=verboseflag)
    #下载单季财报
    else:
        DownloadFR(downloadtype1, yeartype=yeartype1, codenumber=codenumber, downloadflag=downloadflag1, debugflag=verboseflag)

