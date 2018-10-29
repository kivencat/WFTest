# coding:utf-8
import time
from selenium.webdriver.common.by import By
from common.base import Base


class LoginSys(Base):

    def login_sys(self, username, password="1"):
        """
        登录系统
        :param username:  用户名
        :param password: 密码
        :return: null

        """
        login_books_select = (By.ID, "dropdown-select")
        login_username = (By.ID, "username")
        login_password = (By.ID, "psword")
        login_button = (By.CLASS_NAME, "lbtn")
        homepage_tip = (By.CLASS_NAME, "tips-know")

        time.sleep(2)
        self.openurl()
        self.select_dropdown(login_books_select, "1001")
        self.sendkeys(login_username, username)
        self.sendkeys(login_password, password)
        self.click(login_button)
        time.sleep(4)
        self.click(homepage_tip)

    def loginout_sys(self):
        """
        清除cookies，刷新，关闭界面
        :return:
        """
        self.driver.delete_all_cookies()
        self.driver.refresh()
        self.driver.quit()


if __name__ == "__main__":
    from selenium import webdriver
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http://wf74.uf-tobacco.com/sso-webapp/login")
    action_login = LoginSys(driver)
    action_login.login_sys("linhr")




