from common.base import Base
from selenium.webdriver.common.by import By
import datetime
import time
from selenium.webdriver.support.wait import WebDriverWait



class ReqHandle(Base):

    def reqhandle_action(self, vtitle):
        # 需求人员你登录处理需求处理单
        pm_handle_button = (By.XPATH, ".//*[@title='Ctrl+E']")
        pm_requiretype_select = (By.ID, "pk_requiretype")
        pm_requiretype_newprocess = (By.XPATH, ".//*[text()='01 流程新增']")
        pm_vpagename_select = (By.ID, "vpagename")
        pm_vpagename_ylbasepage = (By.XPATH, ".//*[text()='原料管理基础包']")
        pm_vprocesstype_glass = (By.XPATH, ".//*[@id='vprocesstype']/../img")
        pm_vprocesstype_deve = (By.XPATH, ".//*[text()='需求开发']")
        pm_vprocesstype_confirm = (By.XPATH, ".//*[text()='确定']")
        pm_vanalysisreq = (By.ID, "vanalysisreq")
        pm_save_button = (By.XPATH, ".//*[@title='Ctrl+S']")
        pm_prereview_button = (By.XPATH, ".//*[text()='预评审']")

        self.search_todolist_info(vtitle)
        self.switch_to_cardframe()

        self.click(pm_handle_button)
        time.sleep(2)
        self.click(pm_requiretype_select)
        self.click(pm_requiretype_newprocess)
        time.sleep(2)
        self.click(pm_vpagename_select)
        self.click(pm_vpagename_ylbasepage)
        self.click(pm_vprocesstype_glass)
        self.click(pm_vprocesstype_deve)
        self.clicks(pm_vprocesstype_confirm)
        time.sleep(2)
        vana = "需求审批单" + vtitle
        self.sendkeys(pm_vanalysisreq, vana)

        time.sleep(2)
        js = '''document.querySelectorAll("#vreqfilepath+iframe")[0].contentWindow.document.body.innerHTML="富文本测试"'''
        self.driver.execute_script(js)

        self.click(pm_save_button)
        time.sleep(3)
        self.click(pm_prereview_button)

        # 进入预评审单据
        prereview_worknum = (By.ID, "nnum")
        prereview_dplandate = (By.ID, "dplandate")
        prereview_vpreviewnote = (By.ID, "vpreviewnote")
        prereview_save_button = (By.XPATH, ".//*[@title='Ctrl+S']")

        self.switch_to_cardframe()
        self.sendkeys(prereview_worknum, "10")
        # 获取当天日期的七天后
        d_day = datetime.date.today() + datetime.timedelta(days=7)
        s_day = d_day.strftime("%Y-%m-%d")
        self.sendkeys(prereview_dplandate, s_day)
        self.click(prereview_dplandate)

        vpre = "预评审" + vtitle
        self.sendkeys(prereview_vpreviewnote, vpre)


        self.click(prereview_save_button)
