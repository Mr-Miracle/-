from lxml import etree
import requests
from selenium import webdriver
import time
import xlwt

# 这里定义了一个数组，地址中的页码是个变量，这里给变量赋值1到11，不包括11
urls = ['https://cs.lianjia.com/ershoufang/pg{}/'.format(str(i)) for i in range(1, 600)]
for url in urls:
    # 把地址解析成请求
    res = requests.get(url)
    # 把地址请求的页面变成html
    html = etree.HTML(res.text)
    # 用xpath把页面里的指定元素解析到数组中
    # @class是 标签中的class元素
    infos = html.xpath('//ul[@class="sellListContent"]/li')
    # 对数据做循环，把从chrome浏览器中copy的xpath内容黏贴到这里，从里面去掉和infos定义中重复的部分，
    # 也就是去掉//ul[@class="sellListContent"]/li，去掉li之前的内容，只留下后面的部分
    # 在内容后面系上/text()，会把这部分内容解析成文本格式。
    for info in infos:
        title = info.xpath('div[1]/div[1]/a/text()')[0]
        price = info.xpath('div[1]/div[6]/div[1]/span/text()')[0]
        address = info.xpath('div[1]/div[2]/div/a/text()')[0]
        # 多个元素在同一个 区块内，查找规律找到分隔符把他们分开
        room = info.xpath('div[1]/div[2]/div/text()')[0].split(' | ')[1]
        area = info.xpath('div[1]/div[2]/div/text()')[0].split(' | ')[2]
        orient = info.xpath('div[1]/div[2]/div/text()')[0].split(' | ')[3]
        style = info.xpath('div[1]/div[2]/div/text()')[0].split(' | ')[4]
        # 有的内容没有这个部分
        # test1 = info.xpath('div[1]/div[2]/div/text()')[0].split(' | ')[5]
        # 从0开始的，所以如果[5]，就是长度是6，目前的格式[0]没内容
        if len(info.xpath('div[1]/div[2]/div/text()')[0].split(' | ')) == 6:
            lift = info.xpath('div[1]/div[2]/div/text()')[0].split(' | ')[5]
        else:
            lift = '无电梯'
        print(title, '#', price, '#', address, '#', room, '#', area, '#', orient, '#', style, '#', lift)

    #   xlwt.Workbook.add_sheet(infos,'web',title)

    #  xlwt.Workbook.save('‪C:\Users\lujihao\Desktop\web.xlsx')






