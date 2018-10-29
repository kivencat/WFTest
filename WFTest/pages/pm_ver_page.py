from common.base import Base
from selenium.webdriver.common.by import By 
import time


class PMVer(Base):
    def pmver_action(self , vtitle):
        # 需求人员进行验证
        pmver_verify_button = (By.XPATH, ".//*[text()='验证']")
        pmver_confirm = (By.XPATH, ".//*[contains(text(),'定')]")

        self.search_todolist_info(vtitle)
        self.switch_to_cardframe()
        self.click(pmver_verify_button)
        self.clicks(pmver_confirm)
        time.sleep(2)
