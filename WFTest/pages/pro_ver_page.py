from common.base import Base
from selenium.webdriver.common.by import By 


class ProVer(Base):
    def prover_action(self, vtitle):
        # 项目组人员验证
        pt_verify_button = (By.XPATH, ".//*[text()='验证']")
        pt_verify_confirm = (By.XPATH, ".//*[contains(text(),'定')]")
    
        self.search_todolist_info(vtitle)
        self.switch_to_cardframe()
        self.click(pt_verify_button)
        self.clicks(pt_verify_confirm)
