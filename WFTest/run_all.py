import unittest
from common import HTMLTestRunner_cn
# 用例的路径
casePath = r"/Users/sun/Desktop/WFTest"
rule = "test*.py"
discover = unittest.defaultTestLoader.discover(start_dir=casePath, pattern=rule)

reportPath = r"/Users/sun/Desktop/WFTest/report/report.html"

fp = open(reportPath, "wb")

runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,
                                           title="客反平台测试报告",
                                           description="测试基础流程",
                                           retry=0)
runner.run(discover)
fp.close()






