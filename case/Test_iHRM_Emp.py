"""
    测试员工模块的增删改查实现
"""
import unittest
import requests
import logging

import app
from api.empapi import Employee


class Test_Emp(unittest.TestCase):
    def setUp(self):
        self.session = requests.Session()
        self.emp_obj = Employee()
        # self.id = None

    def tearDown(self):
        self.session.close()

    def test_add_emp(self):
        response = self.emp_obj.add_emp(self.session, username='海17', mobile='13121199922',
                                        workNumber='156924')
        print("新增员工：", response.json())
        logging.info('add')
        self.assertEqual(True, response.json().get('success'))
        self.assertEqual(10000, response.json().get('code'))
        self.assertIn('操作成功', response.json().get('message'))
        # 扩大作用域 （为什么self.id 不可以？为什么self.id 变成了方法而不是str?
        #            self.id 无法传递进下一个函数，推测与run_suite有关。
        #            run_suite 内创建了多个对象,确保按顺序执行（本身的执行是并发性的，随机顺序
        # self.id = response.json().get('data').get('id')
        id = response.json().get('data').get('id')
        app.ID = id

    def test_update_emp(self):
        response = self.emp_obj.update_emp(self.session, app.ID, username='海海17')
        print("修改员工：", response.json())
        logging.info('update')
        self.assertEqual(True, response.json().get('success'))
        self.assertEqual(10000, response.json().get('code'))
        self.assertIn('操作成功', response.json().get('message'))

    def test_select_emp(self):
        response = self.emp_obj.select_emp(self.session, app.ID)
        print("查询员工：", response.json())
        logging.info('select')
        self.assertEqual(True, response.json().get('success'))
        self.assertEqual(10000, response.json().get('code'))
        self.assertIn('操作成功', response.json().get('message'))

    def test_delete_emp(self):
        response = self.emp_obj.delete_emp(self.session, app.ID)
        print("删除员工：", response.json())
        logging.info('delete')
        self.assertEqual(True, response.json().get('success'))
        self.assertEqual(10000, response.json().get('code'))
        self.assertIn('操作成功', response.json().get('message'))
