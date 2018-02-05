#coding=utf-8
#author='Shichao-Dong'

import time
from appium import webdriver
from selenium.common.exceptions import WebDriverException
import readConfig
import GetDevices
from StartAppiumServer import Sp
from logs import log

log = log()
conf = readConfig.Readconfig()
cmd = GetDevices.devices()


deviceName = cmd.get_deviceName()
platformVersion = cmd.get_platformVersion().encode('ascii')
platformName = conf.getConfigValue('platformName')
appPackage = conf.getConfigValue('appPackage').encode('ascii')
appActivity = conf.getConfigValue('appActivity').encode('ascii')

s = Sp(deviceName)
appium_port = s.main()


def mydriver():
    desired_caps = {
                'platformName':platformName,'deviceName':deviceName, 'platformVersion':platformVersion,
                'appPackage':appPackage,'appActivity':appActivity,
                'unicodeKeyboard':True,'resetKeyboard':True,'noReset':True
                }
    try:
        driver = webdriver.Remote('http://127.0.0.1:%s/wd/hub'%appium_port,desired_caps)
        time.sleep(4)
        log.info('获取driver成功')
        return driver
    except WebDriverException:
        print 'No driver'


if __name__ == "__main__":

    mydriver()