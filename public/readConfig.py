#coding=utf-8
#author='Shichao-Dong'

import os
import configparser
import codecs

# 获取本文件所在路径
prjDir = os.path.split(os.path.realpath(__file__))[0]
configfile_path = os.path.join(prjDir, "config.ini")

class Readconfig:
    def __init__(self):
        f = open(configfile_path)
        data = f.read()

        self.conf = configparser.ConfigParser()
        self.conf.read(configfile_path)

    def getConfigValue(self,name):
        value = self.conf.get('config',name)
        return value

    def getcmdValue(self,name):
        value = self.conf.get('cmd',name)
        return value

    def getemailValue(self,name):
        value = self.conf.get('email',name)
        return value
