#coding=utf-8
#author='Shichao-Dong'

import sys
reload(sys)
sys.setdefaultencoding('utf8')
import codecs,os
from public.Operate import Operate
from public.GetYaml import getyaml

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
yamlpath = PATH("../../testyaml/pd/pd-001searchpd.yaml")


class SearchpdPage:

    def __init__(self,driver):
        self.path = yamlpath
        self.driver = driver
        self.operate = Operate(self.path,self.driver)

    def operateap(self):
        self.operate.check_operate_type()

    def home(self):
        self.operate.back_home()


# 测试用 忽略
# from public.GetDriver import mydriver
# driver = mydriver()
#
# aa = SearchpdPage(driver)
# aa.operateap()