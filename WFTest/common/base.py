# coding:utf-8
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Base(object):

    def __init__(self, driver):
        """
        初始函数中的变量类中任何方法都可以调用
        :param driver:
        :return:
        """
        self.driver = driver
        self.url = "http://wf74.uf-tobacco.com/sso-webapp/login"

        self.timeout = 20
        self.frequency = 0.5

        self.login_books_select = (By.ID, "dropdown-select")  # 登录页面账套

        self.open_bill_search = (By.ID, "keywordsearch")  # 首页那个搜一搜元素
        self.open_bill_select = (By.XPATH, "//li[@class='ui-menu-item']/a")  # 搜一搜下拉第一条
        self.new_button = (By.ID, "btn_add")  # 所有单据上的新增按钮，要是有个不是就傻逼了。
        self.bill_product = (By.ID, "pk_product")  # 单据上产品字段

    def findelement(self, locator):
        """
        查找某个特定元素
        :param locator:此处为元祖，第一个为找元素的的方式，如By.ID ,第二个为关键字
        :return:这个元素
        """
        # presence_of_element_located 用来检验这个元素是否存在
        try:
            ele = WebDriverWait(self.driver, self.timeout, self.frequency).until(
                EC.presence_of_element_located(locator))
            return ele
        except:
            return False

    def findelements(self, locator):
        """
        查找一组元素
        :param locator: 此处为元祖，第一个为找元素的的方式，如By.ID ,第二个为关键字
        :return: 这组元素
        """
        ele = WebDriverWait(self.driver, self.timeout, self.frequency).until(lambda x: x.find_elements(*locator))
        return ele

    def openurl(self):
        """
        打开客户反馈平台系统
        :return:
        """
        self.driver.get(self.url)
        self.driver.maximize_window()

    def sendkeys(self, locator, text):
        """
        输入字符串
        :param locator: 此处为元祖，第一个为找元素的的方式，如By.ID ,第二个为关键字
        :param text: 输入的字符
        :return:
        """
        ele = self.findelement(locator)
        ele.send_keys(text)

    def sendkeyss(self, locator, text):
        """
        输入字符串，针对所定位元素为一组中最新的一个
        :param locator: 此处为元祖，第一个为找元素的的方式，如By.ID ,第二个为关键字
        :param text: 输入的字符
        :return:
        """
        ele = self.findelements(locator)[-1]
        ele.send_keys(text)

    def click(self, locator):
        """
        点击某元素
        :param locator: 此处为元祖，第一个为找元素的的方式，如By.ID ,第二个为关键字
        :return:
        """
        ele = self.findelement(locator)
        if ele:
            ele.click()
        else:
            pass

    def clicks(self, locator):
        """
        点击某元素，该元素被定位出一组中最新的那个
        :param locator:
        :return:
        """
        ele = self.findelements(locator)[-1]
        ele.click()

    def select_dropdown(self, locator=(By.ID, "dropdown-select"), value="1001"):
        """

        :param locator: 下拉框元素位置
        :param value: 下拉框所要选中的value值
        :return:
        """
        s = self.findelement(locator)
        Select(s).select_by_value(value)

    def open_bill(self, billword):
        """
        通过搜索打开单据
        :param billword: 单据名字
        :return:
        """
        self.findelement(self.open_bill_search).send_keys(billword)
        self.findelement(self.open_bill_select).click()

    def add_bill(self):
        """
        单据新增操作
        :return:
        """
        self.findelement(self.new_button).click()

    def search_todolist_info(self, search_todo_key):
        """
        首页代办搜索
        :param search_todo_key: 搜索的关键字
        :return:
        """
        keyword_box = (By.XPATH, ".//*[text()='输入关键字搜索	']")
        keyword_input_box = (By.ID, "search-keyword")
        keyword_magnifier = (By.XPATH, ".//*[@onclick='searchByKeyWork(this)']")

        time.sleep(2)
        self.findelement(keyword_box).click()
        self.findelement(keyword_input_box).send_keys(search_todo_key)
        self.findelement(keyword_magnifier).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(".//a[contains(@data-content,'%s')]" % search_todo_key).click()

    def switch_to_listframe(self):
        """
        切换到listfram下
        :return:
        """
        time.sleep(2)
        all_handle = self.driver.window_handles
        self.driver.close()
        self.driver.switch_to_window(all_handle[-1])
        time.sleep(1)
        self.driver.switch_to_frame("iframemain")
        self.driver.switch_to_frame("list")
        time.sleep(2)

    def list_to_cardframe(self):
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("iframemain")
        self.driver.switch_to.frame("card")

    def switch_to_cardframe(self):
        """
        切换到card frame下
        :return:
        """
        time.sleep(2)
        all_handle = self.driver.window_handles
        self.driver.close()
        self.driver.switch_to_window(all_handle[-1])
        time.sleep(1)
        self.driver.switch_to_frame("iframemain")
        self.driver.switch_to_frame("card")
        time.sleep(2)

    def is_element_exit(self, locator):
        ele = self.findelement(locator)
        if ele:
            return True
        else:
            return False

    def js_ele_scrollview(self, locator):
        """
        通过js让浏览器滚动到该元素可见区域
        :param locator:
        :return:
        """
        target = self.findelement(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def js_click_byclassname(self, eleinfo):
        """
        通过元素classname找到元素进行js点击
        :param eleinfo:
        :return:
        """
        js = "document.getElementsByClassName('%s')[0].click()" % eleinfo
        self.driver.execute_script(js)

    # def js_click_byxpath(self, xpathinfo):
    #     """
    #     js中通过xpth 定位元素，其中document.evaluate返回xpthresult，iterateNext() 方法返回和一个 XPath 查询匹配的下一个节点。
    #     :param xpathinfo: 所定位元素的xpth
    #     :return:
    #     """
    #     js = '''
    #                           var xresult = document.evaluate\
    #                           (%s, document, null, XPathResult.ANY_TYPE, null);
    #                           var xnodes = [];
    #                           var xres;
    #                           while (xres = xresult.iterateNext()) {
    #                               xnodes.push(xres);
    #                           }
    #                           xnodes[0].click();
    #                      ''' % xpathinfo
    #     self.driver.execute_script(js)

    # js_scroll_totop，js_scroll_tobottom 都是针对非内嵌div的。如果是内嵌了div 就要定位到div 然后用scrollTop
    # 例：js = 'document.getElementsByClassName("scroll")[0].scrollTop=10000' 
    # 例：js = 'document.getElementsByClassName("scroll")[0].scrollLeft=10000' 
    def js_scroll_totop(self):
        """
        通过js移动滚动条到最上面
        :return:
        """
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    def js_scroll_tobottom(self):
        """
        通过js 移动滚动条到最底部
        :return:
        """
        js = "window.scrollTo(0,document.body.scrollHeight"
        self.driver.execute_script(js)

if __name__ == "__main__":
    from selenium import webdriver

    driver = webdriver.Firefox()
    test_driver = Base(driver)
    test_driver.openurl()
    test_driver.login_sys("linhr", "1")
    test_driver.search_todolist_info("请对产品")
    driver.quit()
    driver = webdriver.Firefox()
    test_driver = Base(driver)
    test_driver.openurl()
    test_driver.login_sys("linhr", "1")
    test_driver.open_bill("项目需求填报单")
    test_driver.switch_to_listframe()
    test_driver.add_bill()
    test_driver.list_to_cardframe()
