'''
@Author: Corey He
@Description: 
@Date: 2020-07-31 11:42:51
@LastEditTime: 2020-08-01 12:18:38
@LastEditors: Corey He
@FilePath: \Coreypy\test\testcase\test_Douban.py
'''

import unittest
import sys
sys.path.append('../')
from test.page.DoubanLogin_Page import DoubanLogin_Page
from test.testcase.case_modle import *
from test.common.BrowserDriver import BrowserDriver 
from utils.config import Config

class DoubanCase(model):

    def test_douban_login(self):
        c = Config()
        username = c.get_case_data('test_Douban').get('login').get('username')
        password = c.get_case_data('test_Douban').get('login').get('password')
        
        douban_login = DoubanLogin_Page(self.driver)
        douban_login.login_douban(username,password)
        # douban_login.login_douban("justforcorey@gmail.com","Mogwai@123")


if __name__ == "__main__":
    unittest.main()