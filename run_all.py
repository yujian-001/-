import unittest
from lib.HTMLTestReportCN import HTMLTestRunner
# import lib.HTMLTestReportCN
from config.config import *
from lib.send_email import send_email

logging.info("================================== 测试开始 ==================================")
suite1 = unittest.defaultTestLoader.discover(test_path,pattern="test*.py",top_level_dir=None)  #自动查找test目录下的所有包含test*.py文件的用例

with open(report_file, 'wb') as f:  # 从配置文件中读取，以wb格式打开
    # lib.HTMLTestReportCN.HTMLTestRunner(stream=f, title="Api Test", description="测试描述", tester="卡卡")
    HTMLTestRunner(stream=f, title="Api Test", description="测试描述", tester="卡卡").run(suite1)
    # runner= HTMLTestRunner(stream=f, title="Api Test", description="测试描述", tester="卡卡")
    # runner.run(suite)

send_email(report_file)  # 从配置文件中读取
logging.info("================================== 测试结束 ==================================")
