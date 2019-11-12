"""
    框架搭建：
        核心：api + case + data
            |-- api：封装请求业务（requests）
            |-- case：集成unittest实现，调用api以及参数化解析data
            |-- data：封装测试数据
        报告：report + tools + run_suite.py
            |-- report：保存测试报告
            |-- tools：封装工具文件
            |-- run_suite.py：组织测试套件
        配置：app.py
            |-- app.py：封装程序常量以及配置信息
        日志：log
            |-- log：保存日志信息
"""
import os

# 封装接口的URL前缀
import time

base_url = "http://182.92.81.159"

# 封装项目路径
pro_path = os.path.dirname(os.path.abspath(__file__))
# PRO_PATH = os.getcwd()  获取当前工作目录路径

# 定义一个变量
TOKEN = None

ID = None

import logging
import logging.handlers
# 日志处理
def my_log_config():
    # 获取日志处理器
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    # 设置日志输出目标
    to_1 = logging.StreamHandler()
    filename =  "./log/log" + time.strftime("%Y%m%d%H%M%S") + ".log"
    to_2 = logging.handlers.TimedRotatingFileHandler(filename,when="h",interval=10,backupCount=100,encoding="utf-8")
    # 设置日志写出格式
    formatter = logging.Formatter("%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s")

    # 组织
    to_1.setFormatter(formatter)
    to_2.setFormatter(formatter)
    logger.addHandler(to_1)
    logger.addHandler(to_2)