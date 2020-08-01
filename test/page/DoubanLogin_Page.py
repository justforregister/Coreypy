'''
@Author: Corey He
@Description: 
@Date: 2020-08-01 09:39:28
@LastEditTime: 2020-08-01 12:15:26
@LastEditors: Corey He
@FilePath: \Coreypy\test\page\DoubanLogin_Page.py
'''

import sys
sys.path.append('../')
from selenium.webdriver.common.by import By
from test.common.Seleniums import BasePage
from utils.config import Config

class DoubanLogin_Page(BasePage):
    tab_password_login = (By.XPATH,'//li[@class="account-tab-account"]') #选择密码登陆
    input_username = (By.XPATH,'//input[@id="username"]') 
    input_password = (By.XPATH,'//input[@id="password"]') 
    btn_login = (By.XPATH,'//div[@class="account-form-field-submit "]')
    home_page_arrow_icon = (By.XPATH,'//span[@class="arrow"]') #登陆后账号设置下拉

    def login_douban(self,username,password):
        c = Config()
        url = c.get_case_data('test_Douban').get('login_url')
        self.driver.get(url)
        self.click(self.tab_password_login)
        self.send_key(self.input_username,username)
        self.send_key(self.input_password,password)
        self.click(self.btn_login)
        BasePage.is_visibility(self,self.home_page_arrow_icon)


