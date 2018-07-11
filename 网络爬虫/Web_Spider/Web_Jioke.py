# 抓取糗事百科笑话的脚本
import urllib.request
from bs4 import BeautifulSoup
import time


# 返回文本式的html
def getHTML(url):
    # 给头文件伪装成浏览器访问
    headers = {
        'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    req = urllib.request.Request(url, headers=headers)
    return urllib.request.urlopen(req).read()


# 返回一个bs4_url对象
def creatSoup(url):
    html_text = getHTML(url)
    soup_0 = BeautifulSoup(html_text, 'html5lib')
    return soup_0

# 抓取结束的提示信息,分别是页循环次数和内容循环次数，由于结束之前页和内容循环数还会+1.所以summary要-1
def summaryAllContent(a, b, url):
    print('提示：抓取结束，无更多内容！')
    print('------------------Summary------------------')
    print('您抓取的网址为%s' % url)
    print('共抓取 %d页 共 %d个内容' % (a - 1, b - 1))
    print('-------------------------------------------')


# 得到每一条内容的处理函数，根据不同的html需要修改
def getEachContent(eachContent):
    a = eachContent.select('div')[0]
    b = a.select('span')[0]
    sss = ''
    for s in b.strings:
        sss += s
    return sss

i = 1
k = 1
while i < 3:

    # url = 'https://www.qiushibaike.com/8hr/page/1/?s=4991834' 根据url多页的特性，找到翻页的一个参数
    url = 'https://www.qiushibaike.com/8hr/page/' + str(i) + '/?s=4991834'
    soup = creatSoup(url)
    a_soup = soup.select('a[class=contentHerf]')  # 根据关键字取得按list存放的内容
    contentLen = len(a_soup)  # 取得列表长度
    print('Info: 第%d页有%d个笑话' % (i, contentLen))

    for eachContent in a_soup:
        sss = getEachContent(eachContent)
        print('正在获取第%d个内容...Done' % k)
        time.sleep(0.05)
        k += 1

    print('提示: 正在获取下一页内容...')
    i += 1
    time.sleep(3)


    # 新建文件，新建完在空间中打开，直接使用write写入数据
    def creatExcelAndSheet(sheetName):
        # 新建一个文件
        LJH_TXT = open("F:\PycharmProjects\网络爬虫\Web_Spider\链家租房信息.txt","w")
        LJH_TXT.write("adsssssssssssssssssssssssssss")
        LJH_TXT.close()





