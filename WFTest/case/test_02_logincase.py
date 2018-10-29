# coding:utf-8

import unittest
import ddt
from common.excelutil import ExcelUtil
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from pages.login_page import LoginSys
import os

basepath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
excelPath = os.path.join(basepath, "common", "testdata.xls")


test_excel = ExcelUtil(excelPath)
test_data = test_excel.excelresult()


@ddt.ddt # 在测试类前增加@ddt.ddt
class LoginCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.loginp = LoginSys(self.driver)
        self.loginp.openurl()

    def tearDown(self):
        self.loginp.loginout_sys()

    # 登录用例，而非方法，用例要有期望结果，实际结果进行对比
    def login_case(self, username, password, expect):
        self.loginp.login_sys(username, password)
        notice_pic = (By.CLASS_NAME, "notice")
        time.sleep(2)
        result = self.loginp.is_element_exit(notice_pic)
        self.assertTrue(result == expect)

    @ddt.data(*test_data) # 在测试用例前增加要@ddt.data *test_data list中的字典分组传入
    def test_01(self, data):
        print("---------------开始测试 --------")
        print("测试数据:%s" % data)
        self.login_case(data["username"], data["password"], data["expect"])
        print("--------------结束：pass! --------")







