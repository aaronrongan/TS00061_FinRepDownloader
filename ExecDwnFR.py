
#主执行文件
import csv
from DwnFR_Sina import DownloadFR


codelist=[]

codenumber=input('输入代码：0-根据StockList.csv; 其它-根据实际代码:')
downloadtype1=input('输入年报类型：0-年报；1-一季报；2-中报；3-三季报；[0]:')
yeartype1=input('输入年份: 0-所有年；其它-实际年份;[0]:')
verboseflag=input('是否输出中间信息：0-输出调试信息；1-不输出调试信息;[1]:')
if verboseflag==0:
    verboseflag=True
elif verboseflag==1:
    verboseflag = False
else:
    verboseflag = False


###参数说明
# codenumber = '002271'
# downloadtype = 4  # 4-年报；1-1季报；2-中报；3-3季报；5-招股; 0-4个季度报表全部下载
# downloadflag = True  # True为实际下载，False为不下载
# debugflag = False  # True为输出调试信息，False为不输出
# #yearnumber=0 #

if codenumber ==0 :
    with open('StockList.csv',newline='') as csv_file:
    # with open('StockList.csv',newline='', encoding = 'UTF-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            # print(row['code'],row['name'])
            codelist.append(row['code'])
            if downloadtype1 == 0:
                for each in range(1, 5):
                    DownloadFR(each, yeartype=yeartype1, codenumber=codenumber, downloadflag=True,
                               debugflag=verboseflag)
            else:
                DownloadFR(downloadtype1, yeartype=yeartype1, codenumber=codenumber, downloadflag=True,
                           debugflag=verboseflag)
else:
    if downloadtype1==0:
        for each in range(1, 5):
            DownloadFR(each, yeartype=yeartype1, codenumber=codenumber, downloadflag=True, debugflag=verboseflag)
    else:
        DownloadFR(downloadtype1, yeartype=yeartype1, codenumber=codenumber, downloadflag=True, debugflag=verboseflag)

