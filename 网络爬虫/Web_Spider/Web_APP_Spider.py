from tkinter import *
from lxml import etree
import requests

root = Tk(className='网站数据爬虫程序')
root.geometry('500x400')
label = Label(root,text='网站数据爬虫程序')
label.pack()
def hello():
    print('hello Spider！')

def about():
    w = Label(root,text="开发者感谢\n傅书寰一直以来的支持和陪伴"
                        "\n联系我：QQ邮箱-935184141@qq.com")
    w.pack(side=TOP)

menubar = Menu(root)
#创建下拉菜单File
filemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label="打开", command=hello)
filemenu.add_command(label="保存", command=hello)
filemenu.add_separator()
filemenu.add_command(label="退出", command=root.quit)
menubar.add_cascade(label="文件", menu=filemenu)
#创建另一个下拉菜单Edit
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="剪切", command=hello)
editmenu.add_command(label="复制", command=hello)
editmenu.add_command(label="粘贴", command=hello)
menubar.add_cascade(label="编辑", menu=editmenu)
#创建另一个下拉菜单
selectmenu = Menu(menubar, tearoff=0)
selectmenu.add_command(label="选择全部", command=hello)
selectmenu.add_command(label="选择单行", command=hello)
selectmenu.add_command(label="选择段落", command=hello)
menubar.add_cascade(label="选择",menu=selectmenu)
#创建另一个下拉菜单
foundmenu = Menu(menubar, tearoff=0)
foundmenu.add_command(label="查找...", command=hello)
foundmenu.add_command(label="查找下一个", command=hello)
foundmenu.add_command(label="查找上一个", command=hello)
menubar.add_cascade(label="查找", menu=foundmenu)
#创建下拉菜单Help
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="关于", command=about)
menubar.add_cascade(label="帮助", menu=helpmenu)
#显示菜单
root.config(menu=menubar)

class Application (Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.CreateWidgets()

    def CreateWidgets (self):
        self.nameInput1 = Entry(self,width=35)
        self.nameInput1.pack()
        self.alertButton = Button(self, text='数据爬取',bd='4',command=self.Result)
        self.alertButton.pack()
        self.exchangeButton = Button(self, text='导出数据',bd='4',command=self.ImportData)
        self.exchangeButton.pack()

    def Result(GetData):
        WEB=(GetData.nameInput1.get())
        urls = [WEB.format(str(i)) for i in range(1,2)]
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
                TxtData=['【',title,'】',price,address,room,area,orient,style,lift]

            GetData.Message = Message(GetData,text="正在解析网址。。。", width=300)
            GetData.Message.pack()

        if not GetData.nameInput1.get():
            raise RuntimeError("网址不能为空！")
        else:
            return TxtData

        # 新建文件和使用write写入数据
    def ImportData(TxtFile):
        # 新建一个文件
        LJH_TXT = open("F:\PycharmProjects\网络爬虫\Web_Spider\链家租房信息.txt", "w")
        Txtdata =TxtFile.Result()
        Txtdata="".join(Txtdata)
        LJH_TXT.write(Txtdata)
        LJH_TXT.close()
        TxtFile.Message = Message(TxtFile, text="数据导出完毕", width=300)
        TxtFile.Message.pack()
root = Application()
root.mainloop()

