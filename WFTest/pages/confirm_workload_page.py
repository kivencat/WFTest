from common.base import Base
from selenium.webdriver.common.by import By
import time 


class ConfWorkload(Base):
    def conf_wl_action(self, vtitle):
        # 实施人员确认工作量
        con_workload_confirm = (By.XPATH, ".//*[text()='确认']")
        con_workload_confirmmess = (By.XPATH, ".//*[text()='确认意见:']/../div[1]/textarea ")
        con_workload_confirm2 = (By.XPATH, ".//*[contains(text(),'定')]")

        self.search_todolist_info(vtitle)
        self.switch_to_cardframe()

        self.click(con_workload_confirm)
        self.sendkeys(con_workload_confirmmess, "确认工作量")
        self.clicks(con_workload_confirm2)
        time.sleep(2)
        
