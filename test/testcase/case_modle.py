'''
@Author: Corey He
@Description: 
@Date: 2020-07-31 11:42:51
@LastEditTime: 2020-07-31 16:07:00
@LastEditors: Corey He
@FilePath: \Vantpy\test\testcase\case_modle.py
'''
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
from test.common.BrowserDriver import BrowserDriver
from utils.config import Config
class model(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        c = Config()
        # username = c.get_case_data('login').get('username')
        # password = c.get_case_data('login').get('password')
        driver = BrowserDriver(cls)
        cls.driver = driver.openbrowser(cls)


    def setUp(self):
        pass

    def teardown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()