import tkinter
# 导入线程模块
import threading
import time

root = tkinter.Tk()
root.title('fruits')
root.minsize(300, 300)

# 摆放按钮
btn1 = tkinter.Button(root, text='apple', bg='red')
btn1.place(x=20, y=20, width=50, height=50)

btn2 = tkinter.Button(root, text='pear', bg='white')
btn2.place(x=90, y=20, width=50, height=50)

btn3 = tkinter.Button(root, text='banana', bg='white')
btn3.place(x=160, y=20, width=50, height=50)

btn4 = tkinter.Button(root, text='orange', bg='white')
btn4.place(x=230, y=20, width=50, height=50)

btn5 = tkinter.Button(root, text='litchi', bg='white')
btn5.place(x=230, y=90, width=50, height=50)

btn6 = tkinter.Button(root, text='haw', bg='white')
btn6.place(x=230, y=160, width=50, height=50)

btn7 = tkinter.Button(root, text='cherry', bg='white')
btn7.place(x=230, y=230, width=50, height=50)

btn8 = tkinter.Button(root, text='peach', bg='white')
btn8.place(x=160, y=230, width=50, height=50)

btn9 = tkinter.Button(root, text='lemon', bg='white')
btn9.place(x=90, y=230, width=50, height=50)

btn10 = tkinter.Button(root, text='plum', bg='white')
btn10.place(x=20, y=230, width=50, height=50)

btn11 = tkinter.Button(root, text='grape', bg='white')
btn11.place(x=20, y=160, width=50, height=50)

btn12 = tkinter.Button(root, text='mango', bg='white')
btn12.place(x=20, y=90, width=50, height=50)

# 将所有选项组成列表
fruitlists = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12]

# 是否开启循环的标志
isloop = False
stopsign = False
stopid = None


def round():
    global isloop

    global stopid
    # 判断是否开始循环
    if isloop == True:
        return

    # 初始化计数 变量
    i = 1
    if isinstance(stopid, int):
        i = stopid

    # 死循环
    while 1:

        # 延时操作
        time.sleep(0.2)
        # 将所有的组件背景变为白色
        for x in fruitlists:
            x['bg'] = 'white'

        # 将当前数值对应的组件变色
        fruitlists[i]['bg'] = 'blue'
        # 变量+1
        i += 1

        # 如果i大于最大索引直接归零
        if i >= len(fruitlists):
            i = 0
        if stopsign == True:
            isloop = False
            stopid = i

            break


# 建立一个新线程的函数
def newtask():
    global stopsign

    stopsign = False
    # 建立线程
    t = threading.Thread(target=round)
    # 开启线程运行
    t.start()


def stop1():
    global stopsign

    if stopsign == True:
        return
    stopsign = True


# 开始按钮

btn_start = tkinter.Button(root, text='start', command=newtask, bg='cyan')
btn_start.place(x=90, y=125, width=50, height=50)

# 停止按钮
btn_stop = tkinter.Button(root, text='end', command=stop1, bg='yellow')
btn_stop.place(x=160, y=125, width=50, height=50)

root.mainloop()
