#coding=utf-8
#author='Shichao-Dong'


from page.cm.CmAddcmPage import AddcmPage
from page.cm.CmSortcmPage import SortcmPage



from public.GetDriver import mydriver
from public.StartAppiumServer import Sp
import unittest,time

driver = mydriver()
appiumserver = Sp(driver)

class Cm(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_001addcm(self):
        '''
        新增客户
        :return:
        '''
        add = AddcmPage(driver)
        add.operateap()
        add.home()
    def test_002sortcm(self):
        '''
        客户排序
        :return:
        '''
        sort = SortcmPage(driver)
        sort.sortlist()
        sort.home()

    def test_999close(self):
        driver.quit()
        appiumserver.stop_appium()
        time.sleep(10)

if __name__ == "__main__":
    unittest.main()