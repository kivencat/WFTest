from common.base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.wait import WebDriverWait


class TaskDistribution(Base):
    def taskdis_action(self, vtitle):
        # 开发负责人进入任务分配单
        self.search_todolist_info(vtitle)
        self.switch_to_cardframe()

        taskallocation_handle_button = (By.XPATH, ".//*[@title='Ctrl+E']")
        taskallocation_vreqid = (By.ID, "vreqid")
        taskallocation_overdue = (By.XPATH, ".//*[text()='超期原因']")
        taskallocation_workload = (By.ID, "ext-comp-1013")
        taskallocation_developer = (By.ID, "ext-comp-1023")
        taskallocation_tester = (By.ID, "ext-comp-1030")
        taskallocation_save_button = (By.XPATH, ".//*[@title='Ctrl+S']")
        taskallocation_popwin_confirm = (By.XPATH, ".//*[text()='是']")
        taskallocation_distri_button = (By.XPATH, ".//*[text()='分配']")
        taskallocation_alert_confirm = (By.XPATH, ".//*[text()='是']")

        self.click(taskallocation_handle_button)
        vreqid = self.findelement(taskallocation_vreqid).get_attribute("title")
        vtaskid1 = vreqid + '_1'
        print(vtaskid1)

        '''这一步很有意思，先将滚动条定位到增行按钮附近
           然后用js去点击增行按钮，如果是直接webdriver去进行点击，那么滚动条会滚动盖住元素'''
        self.js_ele_scrollview(taskallocation_overdue)
        time.sleep(3)
        self.js_click_byclassname('uft-grid-header-operator')

        # input 元素需要先点击才出来
        WebDriverWait(self.driver, 3). \
            until(lambda x: x.find_element_by_xpath(".//*[text()='%s']/../../td[10]/div" % vtaskid1)).click()
        time.sleep(1)
        self.sendkeys(taskallocation_workload, Keys.BACK_SPACE)
        self.sendkeys(taskallocation_workload, "3")
        self.sendkeys(taskallocation_workload, Keys.TAB)
        self.driver.find_element_by_xpath(".//*[text()='%s']/../../td[20]/div" % vtaskid1).click()
        self.sendkeys(taskallocation_developer, "肖金龙")
        self.sendkeys(taskallocation_developer, Keys.ENTER)

        # js 根据xpath 获取元素并且点击
        # xpathinfo = './/*[text()="%s"]/../../td[27]/div' % vtaskid1
        # self.js_click_byxpath(xpathinfo)
        # 其中document.evaluate返回xpthresult，iterateNext() 方法返回和一个 XPath 查询匹配的下一个节点。
        js = '''
                       var xresult = document.evaluate\
                       ('.//*[text()="%s"]/../../td[27]/div', document, null, XPathResult.ANY_TYPE, null);
                       var xnodes = [];
                       var xres;
                       while (xres = xresult.iterateNext()) {
                           xnodes.push(xres);
                       }
                       xnodes[0].click();
                  ''' % vtaskid1
        self.driver.execute_script(js)


        self.sendkeys(taskallocation_tester, "杨月如")
        time.sleep(2)
        self.click(taskallocation_save_button)
        self.clicks(taskallocation_popwin_confirm)
        time.sleep(2)
        self.click(taskallocation_distri_button)
        time.sleep(2)
        self.clicks(taskallocation_alert_confirm)
        time.sleep(2)
