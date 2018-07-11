#coding:utf-8

from selenium import webdriver
import time
import xlwt


driver = webdriver.Chrome()
driver.get("http://xxxx/")
time.sleep(2)


#登陆研究生系统
driver.find_element_by_name("userName").send_keys("xxx")
driver.find_element_by_name("password").send_keys("xxx")
time.sleep(2)
driver.find_element_by_xpath("html/body/div[2]/div[1]/form/div/dl/dt[3]/input[3]").click()
time.sleep(2)
driver.find_element_by_class_name("img_dl").click()

#跳转到成绩查询按钮的frame
frame1 = driver.find_element_by_name("leftFrame")
driver.switch_to.frame(frame1)
iframe1 = driver.find_element_by_name("zbFrame")
driver.switch_to.frame(iframe1)
time.sleep(3)
#点击成绩查询-学期成绩查询
driver.find_element_by_xpath("html/body/table/tbody/tr/td/div/div/table[4]/tbody/tr/td/a").click()
driver.find_element_by_xpath("html/body/table/tbody/tr/td/div/div/div[4]/table/tbody/tr/td/a").click()

#先回到原来的页面
driver.switch_to.default_content()
#载跳转到查询按钮所在的frame
frame2 = driver.find_element_by_name("mainFrame")
driver.switch_to.frame(frame2)
#点击查询按钮
driver.find_element_by_xpath("//button[@class='button2']").click()

#创建工作簿
wbk = xlwt.Workbook(encoding='utf-8', style_compression=0)
#创建工作表
sheet = wbk.add_sheet('sheet 1', cell_overwrite_ok=True)

def save_Data():
    #table_list=[]
    #row_list=[]
    #表头
    table_top_list = driver.find_element_by_xpath("//form[@name='studentForm']/div[3]/fieldset/table/thead/tr").find_elements_by_tag_name('td')
    for c,top in enumerate(table_top_list):
        #row_list.append(top.text)
        sheet.write(0, c, top.text)
    #table_list.append(row_list)

    # 表的内容
    #将表的每一行存在table_tr_list中
    table_tr_list = driver.find_element_by_xpath("//form[@name='studentForm']/div[3]/fieldset/table/tbody").find_elements_by_tag_name('tr')
    #每行输出到row_list中,将所有的row_list输入到table_list中
    for r,tr in enumerate(table_tr_list,1):
        #将表的每一行的每一列内容存在table_td_list中
        table_td_list = tr.find_elements_by_tag_name('td')
        #将行列的内容加入到table_list中
        for c,td in enumerate(table_td_list):
            #row_list.append(td.text)
            sheet.write(r, c, td.text)
            #print td.text
        #table_list.append(row_list)
    #最后返回table_list
    #return table_list

save_Data()
#保存该文件，文件必须存在
wbk.save(r'C:\xxx\test.xls')

#先回到原来的页面
driver.switch_to.default_content()
print ('done')