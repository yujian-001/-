import unittest
import requests
import json
import sys
import os
sys.path.append('../..')

from config.config import *
from lib.db import *
from lib.read_excel import *
from lib.case_log import log_case_info

#账号注册操作
class TestUserReg(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # cls.data_list = excel_to_list(os.path.join(data_path, "test_user_data.xlsx"), "TestUserReg")  # 读取TestUserReg工作簿的所有数据
        cls.data_list = excel_to_list(data_path,"TestUserReg")  # 读取TestUserReg工作簿的所有数据

    #正常注册操作
    def test_user_reg_normal(self):
        case_data = get_test_data(self.data_list, 'test_user_reg_normal')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = json.loads(case_data.get('data'))# 转为字典，需要取里面的name进行数据库检查
        expect_res = json.loads(case_data.get('expect_res'))  # 转为字典，断言时直接断言两个字典是否相等

        name = data.get("name")

        # 环境检查,检查用户是否已注册，已注册，删除数据库的用户
        if check_user(name):
            del_user(name)
        # 发送请求
        headers={"Content-Type":"application/json"}
        res = requests.post(url=url, data=json.dumps(data),headers=headers)

        result=res.json() #result为字典格式
        log_case_info('test_user_reg_normal', url, data, expect_res, result)

        # 响应断言（整体断言）
        self.assertDictEqual(result,expect_res) #将res响应的内容转换为字典格式

        # 数据库断言
        # self.assertTrue(check_user(name))

        # 环境清理（由于注册接口向数据库写入了用户信息）
        del_user(name)

    # #用户名已存在注册操作
    def test_user_reg_exist(self):
        case_data = get_test_data(self.data_list, 'test_user_reg_exist')
        if not case_data:
            print("用例数据不存在")
        url = case_data.get('url')
        data = json.loads(case_data.get('data'))  # 转为字典，需要取里面的name进行数据库检查
        expect_res = json.loads(case_data.get('expect_res'))  # 转为字典，断言时直接断言两个字典是否相等
        name = data.get("name")

        # 环境检查
        if not check_user(name):
            add_user(name, '123456')
        headers={"Content-Type":"application/json"}

      # 发送请求,data是json格式的数据
        res=requests.post(url=url,data=json.dumps(data),headers=headers)
        result=res.json()

        log_case_info('test_user_reg_exist', url, data, expect_res, result)

        # 响应断言（整体断言）,res.json()为json格式的字符串
        self.assertDictEqual(result, expect_res)



if __name__ == '__main__':
    unittest.main(verbosity=2)  # 运行所有用例
