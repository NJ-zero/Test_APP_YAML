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
yamlpath = PATH("../../testyaml/cm/cm-002sortcm.yaml")


class SortcmPage:

    def __init__(self,driver):
        self.path = yamlpath
        self.driver = driver
        self.operate = Operate(self.path,self.driver)

    def sortlist(self):
        self.operate.check_operate_type()

    def home(self):
        self.operate.back_home()