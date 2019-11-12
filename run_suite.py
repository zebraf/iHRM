"""
    测试套件
        按照需求组合被执行的测试函数
"""
# 导包
import unittest
# 实例化套件对象，组织被执行的测试函数
import time

from case.Test_iHRM_Emp import Test_Emp
from case.Test_iHRM_Login import Test_Login
from tools.HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()
suite.addTest(Test_Login('test_login_success'))
suite.addTest(Test_Emp('test_add_emp'))
suite.addTest(Test_Emp('test_update_emp'))
suite.addTest(Test_Emp('test_select_emp'))
suite.addTest(Test_Emp('test_delete_emp'))
# 执行套件，生成测试报告
with open("./report/report.html", "wb") as f:
    # 使用 HTMLTestRunner 运行测试套件，将结果写入文件流
    runner = HTMLTestRunner(stream=f, title="iHRM员工模块增删改查接口测试",
                              description='系统：win10,语言：python')
    runner.run(suite)
