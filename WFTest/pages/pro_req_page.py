from common.base import Base
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class ProReq(Base):

    def proreq_add_action(self):
        self.open_bill("项目需求填报单")
        #  切换窗口,切换框架
        self.switch_to_listframe()
        time.sleep(2)
        self.add_bill()
    
    def proreq_card_action(self, vtitle):
    
        req_product = (By.ID, "pk_product")  # 产品名称
        req_title = (By.ID, "vreqtitle")  # 需求标题
        req_voriginalreq = (By.ID, "voriginalreq")
        req_save_button = (By.CLASS_NAME, "btnSave")  # 保存按钮
        req_submit_button = (By.ID, "btn_commit")  # 提交按钮
        req_approvedby = (By.XPATH, ".//*[text()='(linhr)林华瑞']")  # 审批流指派界面linhr
        # 审批流指派界面向右箭头图标
        req_choice_approve = (By.XPATH, "//*[@src='/webnc-resource-webapp/theme/web_blue/images/app/right.gif']")
        req_approve_confirm = (By.XPATH, ".//*[text()='确定']")  # 审批流指派界面确定按钮
        home_page = (By.XPATH, ".//*[text()='首页']")  # 首页按钮
        home_page_point = (By.ID, "PanelBusiAnaly")
        req_approve_button = (By.XPATH, ".//*[text()='审核']")
        req_approve_comment = (By.XPATH, ".//*[@class='txt-area']")
        req_approve_approve = (By.XPATH, ".//*[text()='批准']")
        req_treatment = (By.XPATH, ".//*[text()='处理情况']")
        req_pm = (By.XPATH, ".//*[text()='需求处理单']/../../td[4]/div")
        req_treatment_close = (By.XPATH, ".//*[@class='x-tool x-tool-close']")
    

        self.list_to_cardframe()
    
        # 填写项目需求填报单
        time.sleep(5)
        self.sendkeys(req_product, "原料")
        self.sendkeys(req_product, Keys.TAB)
        # current_time = time.time()
        # vtitle = "test" + str(current_time)
        print(vtitle)
        self.sendkeys(req_title, vtitle)
        time.sleep(2)
        self.sendkeys(req_voriginalreq, vtitle)
    
        # 保存，提交项目需求填报单
        self.click(req_save_button)
        time.sleep(5)
        self.click(req_submit_button)
        time.sleep(3)
    
        # 选择审批人进行提交
        self.click(req_approvedby)
        time.sleep(2)
        self.click(req_choice_approve)
        time.sleep(2)
        self.clicks(req_approve_confirm)
        time.sleep(2)
    
        # 回首页
        self.driver.switch_to.default_content()
        self.click(home_page)
        # 因为回到首页鼠标还悬停在菜单上会有下拉框，所以悬停到旁边
        time.sleep(3)
        temp_point = self.findelement(home_page_point)
        webdriver.ActionChains(self.driver).move_to_element(temp_point).perform()
        self.search_todolist_info(vtitle)
        self.switch_to_cardframe()
    
        # 审核项目需求填报单
        self.click(req_approve_button)
        self.sendkeys(req_approve_comment, "审批通过！")
        self.click(req_approve_approve)

        # 获取需求人员是谁
        self.click(req_treatment)
        pm = self.findelement(req_pm).text
        self.click(req_treatment_close)



