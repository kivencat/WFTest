from common.base import Base
from selenium.webdriver.common.by import By
import time


class TaskDev(Base):
    def taskdev_action(self, vtitle):
        # 开发人员登陆点击开发完成
        devtask_complete_button = (By.XPATH, ".//*[text()='开发完成']")
        devtask_solution_ins = (By.XPATH, ".//*[text()='开发解决说明:']/../div[1]/textarea")
        devtask_solution_cofirm = (By.XPATH, ".//*[contains(text(),'定')]")

        self.search_todolist_info(vtitle)
        self.switch_to_cardframe()
        self.click(devtask_complete_button)
        self.sendkeyss(devtask_solution_ins, "开发完成")
        self.clicks(devtask_solution_cofirm)
        time.sleep(2)
