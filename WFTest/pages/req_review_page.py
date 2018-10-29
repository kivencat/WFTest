from common.base import Base
from selenium.webdriver.common.by import By
import time                                      


class ReqReview(Base):
    def reqreview_action(self, vtitle):
        # 需求人员进行需求正式评审
        forreview_handle_button = (By.XPATH, ".//*[@title='Ctrl+E']")
        forreview_save_button = (By.XPATH, ".//*[@title='Ctrl+S']")
        forreview_pass_button = (By.XPATH, ".//*[text()='评审通过']")
        forreview_pass_opinion = (By.XPATH, ".//*[text()='评审意见:']/../div[1]/textarea ")
        forreview_pass_confirm = (By.XPATH, ".//*[contains(text(),'定')]")

        self.search_todolist_info(vtitle)
        self.switch_to_cardframe()
        self.click(forreview_handle_button)
        self.click(forreview_save_button)
        time.sleep(2)
        self.click(forreview_pass_button)
        self.sendkeys(forreview_pass_opinion, "评审通过")
        self.clicks(forreview_pass_confirm)
