#####定义全局变量
#下载地址
#文件命名规则
#错误提示

#下载地址
url_ar_sample='http://vip.stock.finance.sina.com.cn/corp/go.php/vCB_Bulletin/stockid/002271/page_type/ndbg.phtml'
global url_ar_1,url_ar_2
url_ar_1='http://vip.stock.finance.sina.com.cn/corp/go.php/vCB_Bulletin/stockid/'
url_ar_2='/page_type/ndbg.phtml'

global url_q1_1
url_q1='http://vip.stock.finance.sina.com.cn/corp/go.php/vCB_BulletinYi/stockid/002271/page_type/yjdbg.phtml'
url_q1_1='http://vip.stock.finance.sina.com.cn/corp/go.php/vCB_Bulletin/stockid/'
url_q1_2='/page_type/yjdbg.phtml'

global url_q2_1
url_q2='http://vip.stock.finance.sina.com.cn/corp/go.php/vCB_BulletinZhong/stockid/002271/page_type/zqbg.phtml'
url_q2_1='http://vip.stock.finance.sina.com.cn/corp/go.php/vCB_Bulletin/stockid/'
url_q2_2='/page_type/zqbg.phtml'

global url_q3_1
url_q3='http://vip.stock.finance.sina.com.cn/corp/go.php/vCB_BulletinSan/stockid/002271/page_type/sjdbg.phtml'
url_q3_1='http://vip.stock.finance.sina.com.cn/corp/go.php/vCB_Bulletin/stockid/'
url_q3_2='/page_type/sjdbg.phtml'

global url_zhaogu
# url_zhaogu_sample='http://vip.stock.finance.sina.com.cn/corp/view/vCB_Bulletin.php/page_type/zgsmsyxs.phtml?stockid=002271'
url_zhaogu_sample='http://vip.stock.finance.sina.com.cn/corp/go.php/vCB_BulletinSan/stockid/002271/page_type/zgsmsyxs.phtml'
# url_zhaogu='http://vip.stock.finance.sina.com.cn/corp/view/vCB_Bulletin.php/page_type/zgsmsyxs.phtml?stockid='
url_zhaogu_1='http://vip.stock.finance.sina.com.cn/corp/go.php/vCB_Bulletin/stockid/'
url_zhaogu_2='/page_type/zgsmsyxs.phtml'

#下载文件目录
global downloadpath1,downloadpath2
downloadpath1='I://MyMobileBooks_800_FinRep//'
downloadpath2='C:/Users/aaron/Documents/MyMobileBooks_800_FinRep/'

#下载文件命名规格
global filename_ar,filename_q1,filename_q2,filename_q3,filename_zhaogu
filename_ar_sample='002271_2018_年度报告'
filename_ar='_年度报告'

filename_q1_sample='002271_2018_一季报告'
filename_q1='_一季报告'

filename_q2_sample='002271_2018_年中报告'
filename_q2='_年中报告'

filename_q3_sample='002271_2018_三季报告'
filename_q3='_三季报告'

filename_zhaogu_sample='002271_招股说明书'
filename_zhaogu='_招股说明书'


#错误提示
global msg1, msg2
msg1='没有此时的报表，无法下载'
msg2='文件已存在，是否要覆盖？'