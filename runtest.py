#coding=utf-8
#author='Shichao-Dong'

import time,os
import unittest
import HTMLTestRunner
from testcase.CmTest import Cm


def testsuit():
    suite = unittest.TestSuite()
    suite.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(Cm),




])

    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)

    now=time.strftime("%y-%m-%d-%H-%M-%S")
    PATH = lambda p: os.path.abspath(
        os.path.join(os.path.dirname(__file__), p)
    )
    dirpath = PATH("./results/waiqin365-")

    filename=dirpath + now +'result.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='waiqin365 6.0.6beta test result',description=u'result:')

    runner.run(suite)
    fp.close()

if __name__ =="__main__":
    testsuit()