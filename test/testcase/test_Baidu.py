'''
@Author: Corey He
@Description: 
@Date: 2020-07-31 11:42:51
@LastEditTime: 2020-07-31 16:20:03
@LastEditors: Corey He
@FilePath: \Vantpy\test\testcase\test_Baidu.py
'''

import unittest
import sys
sys.path.append('../')
from test.page.BaiduPage import BaiduPage
from test.testcase.case_modle import *
from test.common.BrowserDriver import BrowserDriver

class BaiduCase(model):

    def test_baidu1(self):
        baidu = BaiduPage(self.driver)
        baidu.input_baidu_text('selenium')
        baidu.click_baidu_btn()
        # baidu.get_screent_img("baidu")
        self.assertIn('selenium',self.driver.title)
