#coding=utf-8
#author='Shichao-Dong'

from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from logs import log
import os
import time


'''
一些基础操作：滑动、截图、点击页面元素等
'''

log = log()
# driver = GetDriver.mydriver()

class BaseOperate:
    def __init__(self,driver):
        self.driver = driver

    def back(self):
        '''
        返回键
        :return:
        '''
        os.popen("adb shell input keyevent 4")

    def get_window_size(self):
        '''
        获取屏幕大小
        :return: windowsize
        '''
        global windowSize
        windowSize = self.driver.get_window_size()
        return windowSize

    def swipe_up(self):
        '''
        向上滑动
        :return:
        '''
        windowsSize = self.get_window_size()
        width = windowsSize.get("width")
        height = windowsSize.get("height")
        self.driver.swipe(width/2, height*3/4, width/2, height/4, 1000)

    def screenshot(self):
        now=time.strftime("%y%m%d-%H-%M-%S")
        PATH = lambda p: os.path.abspath(
            os.path.join(os.path.dirname(__file__), p)
        )
        screenshoot_path = PATH('../results/screenshoot/failpic')
        self.driver.get_screenshot_as_file(screenshoot_path+now+'.png')

    def find_id(self,id):
        '''
        寻找元素
        :return:
        '''
        try:
            exsit = self.driver.find_element_by_id(id)
            return True
        except:
            log.error('未定位到元素：'+'%s'%(id))
            self.screenshot()
            return False

    def find_name(self,name):
        '''
        判断页面是否存在某个元素
        :param name: text
        :return:
        '''
        findname = "//*[@text='%s']"%(name)
        try:
            exsit = self.driver.find_element_by_xpath(findname)
            return True
        except:
            log.error('未定位到元素：'+'%s'%(name))
            self.screenshot()
            return False

    def get_name(self,name):
        '''
        定位页面text元素
        :param name:
        :return:
        '''
        # element = driver.find_element_by_name(name)
        # return element

        findname = "//*[@text='%s']"%(name)
        try:
            # element = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(findname))
            WebDriverWait(
            self.driver, 15).until(
            lambda driver: driver.find_element_by_xpath(findname).is_displayed())
            element = self.driver.find_element_by_xpath(findname)
            return element
        except:
            self.screenshot()
            log.error('未定位到元素：'+'%s'%(name))

    def get_id(self,id):
        '''
        定位页面resouce-id元素
        :param id:
        :return:
        '''
        try:
            # element = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id(id()))

            WebDriverWait(
            self.driver, 15).until(
            lambda driver: driver.find_element_by_id(id).is_displayed())
            self.driver.implicitly_wait(2)
            element = self.driver.find_element_by_id(id)
            return element
        except:
            self.screenshot()
            log.error('未定位到元素：'+'%s'%(id))

    def get_xpath(self,xpath):
        '''
        定位页面xpath元素
        :param id:
        :return:
        '''
        try:
            # element = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(xpath))
            WebDriverWait(
            self.driver, 15).until(
            lambda driver: driver.find_element_by_xpath(xpath).is_displayed())
            element = self.driver.find_element_by_xpath(xpath)
            return element
        except:
            self.screenshot()
            log.error('未定位到元素：'+'%s'%(xpath))

    def get_ids(self,id):
        '''
        定位页面resouce-id元素组
        :param id:
        :return:列表
        '''
        try:
            # elements = self.driver.find_elements_by_id(id)
            elements = WebDriverWait(self.driver, 10).until(lambda x: x.find_elements_by_id(id))
            self.driver.implicitly_wait(2)
            return elements
        except:
            self.screenshot()
            log.error('未定位到元素：'+'%s'%(id))

    def page(self,name):
        '''
        返回至指定页面
        :return:
        '''
        i=0
        while i<10:
            i=i+1
            try:
                findname = "//*[@text='%s']"%(name)
                self.driver.find_element_by_xpath(findname)
                self.driver.implicitly_wait(2)
                break
            except :
                os.popen("adb shell input keyevent 4")
                try:
                    findname = "//*[@text='确定']"
                    self.driver.find_element_by_xpath(findname).click()
                    self.driver.implicitly_wait(2)
                except:
                    os.popen("adb shell input keyevent 4")
                try:
                    self.driver.find_element_by_xpath("//*[@text='工作台']")
                    self.driver.implicitly_wait(2)
                    break
                except:
                    os.popen("adb shell input keyevent 4")