from selenium import webdriver
import time
import os
#环境配置
chromedriver = "C:\\Users\\kcadmin\\AppData\\Local\\Google\\Chrome\\Application"
os.environ["webdriver.Chrome.driver"] = chromedriver
web_driver = webdriver.Chrome()  #创建浏览器驱动对象
web_driver.implicitly_wait(30)
#进入该网页，点击登录按钮，跳转到登录页面
web_driver.get('https://www.euserv.com/en/')
web_driver.find_element_by_link_text('Login Customer Panel').click()
#实现不同的窗口切换
handles = web_driver.window_handles
print(handles)
web_driver.switch_to_window(handles[1])
#输入用户名或密码进行登录
web_driver.find_element_by_name('email').send_keys('e@sjhz.cf')
web_driver.find_element_by_name('password').send_keys('vwv56ty7')
web_driver.find_element_by_name('Submit').click()
#进入登录页面



#关闭浏览器