import json
import sys
sys.path.append('..') #添加..到环境变量中(当摸个模块不能导入其他模块时)
# print(sys.path)
from config.config import *


def log_case_info(case_name, url, data, expect_res, res):
    if isinstance(data,dict): #isinstance(用例判断一个对象是否是一个已知对象，True or False)
        data = json.dumps(data, ensure_ascii=False)  # 如果data是字典格式，转化为字符串
    logging.info("测试用例：{}".format(case_name))
    logging.info("url：{}".format(url))
    logging.info("请求参数：{}".format(data))
    logging.info("期望结果：{}".format(expect_res))
    logging.info("实际结果：{}".format(res))

# if __name__=="__main__": #在test_user_login.py调用log_case_info()函数
#     log_case_info('test_user_login_normal, url, data, expect_res, res.text')
