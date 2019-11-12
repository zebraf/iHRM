"""
    封装unittest相关实现
"""
# 导包
import json
import unittest
import requests

import app
from api.loginapi import Login
# 参数化步骤：导包
from parameterized import parameterized


# 参数化步骤：解析
def bulid_data():
    data = []
    with open(app.pro_path + '/data/login_data.json', 'r', encoding='utf-8') as f:
        for i in json.load(f).values():
            mobile = i.get('mobile')
            password = i.get('password')
            success = i.get('success')
            code = i.get('code')
            message = i.get('message')
            ele = (mobile, password, success, code, message)
            data.append(ele)
    return data


class Test_Login(unittest.TestCase):
    def setUp(self):
        self.session = requests.Session()
        self.login_obj = Login()

    def tearDown(self):
        self.session.close()

    @parameterized.expand(bulid_data())
    def test_login(self, mobile, password, success, code, message):
        print('-' * 100)
        print('参数化读取的数据', mobile, password, success, code, message)
        response = self.login_obj.login(self.session, mobile, password)
        print('响应结果', response.json())
        su = response.json().get('success')
        co = response.json().get('code')
        me = response.json().get('message')
        self.assertEqual(success, su)
        self.assertEqual(code, co)
        self.assertIn(message, me)

    # 编写登录成功的测试函数
    def test_login_success(self):
        response = self.login_obj.login(self.session,'13800000002','123456')
        print('-'*100)
        print('登录成功响应结果：',response.json())
        self.assertEqual(True, response.json().get('success'))
        self.assertEqual(10000, response.json().get('code'))
        self.assertIn('操作成功', response.json().get('message'))
        # 提取token
        token = response.json().get('data')
        # 预期允许其他文件调用该token值，可以扩大token的作用域（将token赋值给app的一个全局变量）
        app.TOKEN = token
