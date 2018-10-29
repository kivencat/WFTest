# conding = uft-8
from selenium import webdriver
import time
from pages.login_page import LoginSys
from pages.pro_req_page import ProReq
from pages.req_handle_page import ReqHandle
from pages.confirm_workload_page import ConfWorkload
from pages.req_review_page import ReqReview
from pages.task_dis_page import TaskDistribution
from pages.task_dev_page import TaskDev
from pages.test_ver_page import TestVer
from pages.pm_ver_page import PMVer
from pages.pro_ver_page import ProVer
from pymouse import PyMouse
from pykeyboard import PyKeyboard
import unittest


class TestFlow(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        #cls.driver = webdriver.Ie()
        cls.loginp = LoginSys(cls.driver)
        cls.proreq = ProReq(cls.driver)

    def test_01_baseflow(self):
        current_time = time.time()
        vtitle = "test" + str(current_time)

        # 填写需求填报单
        self.loginp.login_sys("linhr")
        self.proreq.proreq_add_action()
        self.proreq.proreq_card_action(vtitle)
        time.sleep(2)
        self.loginp.loginout_sys()

        # 需求预评审
        self.driver = webdriver.Firefox()
        self.reqhandle = ReqHandle(self.driver)
        self.login_reqhandle = LoginSys(self.driver)
        self.login_reqhandle.login_sys("wulj")
        self.reqhandle.reqhandle_action(vtitle)
        time.sleep(2)
        self.login_reqhandle.loginout_sys()

        # 工作量确认
        self.driver = webdriver.Firefox()
        self.conwork = ConfWorkload(self.driver)
        self.login_confwork = LoginSys(self.driver)
        self.login_confwork.login_sys("linhr")
        self.conwork.conf_wl_action(vtitle)
        time.sleep(2)
        self.login_confwork.loginout_sys()

        # 需求正式评审
        self.driver = webdriver.Firefox()
        self.reqrev = ReqReview(self.driver)
        self.login_reqrev = LoginSys(self.driver)
        self.login_reqrev.login_sys("wulj")
        self.reqrev.reqreview_action(vtitle)
        time.sleep(2)
        self.login_reqrev.loginout_sys()

        # 任务分配单
        self.driver = webdriver.Firefox()
        self.taskdis = TaskDistribution(self.driver)
        self.login_taskdis = LoginSys(self.driver)
        self.login_taskdis.login_sys("lijx")
        self.taskdis.taskdis_action(vtitle)
        time.sleep(2)
        self.login_taskdis.loginout_sys()

        # 开发任务单
        self.driver = webdriver.Firefox()
        self.taskdev = TaskDev(self.driver)
        self.login_taskdev = LoginSys(self.driver)
        self.login_taskdev.login_sys("xiaojl")
        self.taskdev.taskdev_action(vtitle)
        time.sleep(2)
        self.login_taskdev.loginout_sys()

        #  测试验证
        self.driver = webdriver.Firefox()
        self.testver = TestVer(self.driver)
        self.login_testver = LoginSys(self.driver)
        self.login_testver.login_sys("yangyr")
        self.testver.testver_action(vtitle)
        time.sleep(2)
        self.login_testver.loginout_sys()

        #  需求验证
        self.driver = webdriver.Firefox()
        self.pmver = PMVer(self.driver)
        self.login_pmver = LoginSys(self.driver)
        self.login_pmver.login_sys("wulj")
        self.pmver.pmver_action(vtitle)
        time.sleep(2)
        self.login_pmver.loginout_sys()

        # 项目组验证
        self.driver = webdriver.Firefox()
        self.prover = ProVer(self.driver)
        self.login_prover = LoginSys(self.driver)
        self.login_prover.login_sys("linhr")
        self.prover.prover_action(vtitle)
        time.sleep(2)
        self.login_prover.loginout_sys()
        # 断言
        self.assertTrue(1 == 1)

    @classmethod
    def tearDownClass(cls):
        print("the test_01 case is over！")


if __name__ == "__main__":
    unittest.main()




