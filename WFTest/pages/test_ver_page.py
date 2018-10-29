# conding = uft-8
from common.base import Base
from selenium.webdriver.common.by import By 
import time
from pymouse import PyMouse
from pykeyboard import PyKeyboard
import os


class TestVer(Base):
    def testver_action(self, vtitle):
        # 测试人员登陆点击测试完成
        testver_pass_button = (By.XPATH, ".//*[text()='测试验证通过']")
        testver_solve_method = (By.XPATH, ".//*[text()='解决方式:']/../div[1]/div/img")
        # testver_plate = (By.XPATH, ".//div[text()='安装盘']")
        testver_plate = (By.XPATH, ".//div[text()='补丁']")
        # testver_version = (By.XPATH, ".//*[text()='最终版本号:']/../div[1]/textarea")
        testver_browse = (By.ID, "patchfileupload_id")
        testver_confirm_button = (By.XPATH, ".//*[contains(text(),'定')]")

        self.search_todolist_info(vtitle)
        self.switch_to_cardframe()

        self.click(testver_pass_button)
        self.click(testver_solve_method)
        self.click(testver_plate)
        self.click(testver_browse)
        time.sleep(2)
        pathname="C:\\Users\\sun\\Desktop\\WFTest\\common\\nc60-20181022-WF厦门烟草180024-abc.zip"
        os.system(r"C:\Users\sun\Desktop\WFTest\common\up-Script.au3 %s" % pathname)

        # # 用PyKeyboard对win窗口操作
        # k = PyKeyboard()
        # pathname = '''C:\Users\sun\Desktop\WFTest\common\nc60-20181022-WF180024-abc.zip'''      #此种方式不能输入中文
        # # k.press_key(k.shift_key)
        # # k.tap_key(k.control_key)
        #
        # for i in pathname:
        #     k.tap_key(i)
        # time.sleep(1)
        # k.tap_key(k.enter_key, n = 2, interval = 5)   #连续两次点击


        self.clicks(testver_confirm_button)
        time.sleep(2)
if __name__ == "__main__":
    # conding = uft-8
    from selenium import webdriver
    from pages.login_page import LoginSys

    driver = webdriver.Firefox()

    # 继承多个父类的用法
    class TDriver(LoginSys, TestVer):
        pass

    c = TDriver(driver)
    c.login_sys("yangyr")
    c.testver_action("test1540622988.4411755")




