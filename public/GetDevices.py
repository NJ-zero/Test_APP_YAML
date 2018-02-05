#coding=utf-8
#author='Shichao-Dong'

import os
import readConfig
from logs import log

conf = readConfig.Readconfig()
log = log()

class devices:
    def __init__(self):
        self.get_device = conf.getcmdValue('viewPhone')
        self.get_Version = conf.getcmdValue('viewAndroid')
        self.startServer = conf.getcmdValue('startServer')

    def get_deviceName(self):
        values = os.popen(self.get_device).readlines()
        dev = values[1].split()[0]
        if len(values)-2 == 1:
            print dev
            log.info('手机设备为：'+dev)
            return dev
        else:
            log.warn('暂未获取到手机设备')
            print 'No device found'

    def get_platformVersion(self):
        values = os.popen(self.get_Version).readlines()

        if values != '':
            Version=values[0].split('=')[1]
            print Version
            log.info('手机版本号为：'+Version)
            return Version.strip()
        else:
            log.warn('暂未获取到手机设备')
            print 'No device found'



if __name__ == '__main__':
    cmd = devices()
    cmd.get_deviceName()
    cmd.get_platformVersion()