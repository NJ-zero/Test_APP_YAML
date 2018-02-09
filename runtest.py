#coding=utf-8
#author='Shichao-Dong'

import time,os
import unittest
import HTMLTestRunner
import smtplib
import datetime
from public.readConfig import Readconfig
from public.Sendemail import Email
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.header import Header
from email.mime.multipart import MIMEMultipart

# from testcase.CmTest import Cm


PATH = lambda p: os.path.abspath(
        os.path.join(os.path.dirname(__file__), p)
    )

def testsuit():
    suite = unittest.TestSuite()
    suite.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(Cm),




])

    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)

    now=time.strftime("%y-%m-%d-%H-%M-%S")
    dirpath = PATH("./results/waiqin365-")

    filename=dirpath + now +'result.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='waiqin365 6.0.6beta test result',description=u'result:')

    runner.run(suite)
    fp.close()


def send_email():
    #定义发件箱
    conf = Readconfig()
    smtpsever = conf.getemailValue('smtpsever')
    user = conf.getemailValue('user')
    password = conf.getemailValue('password')
    sender = conf.getemailValue('sender')
    receiver = conf.getemailValue('receiver')

    sendemail = Email()
    msg=sendemail.email()

    #发送邮件
    smtp=smtplib.SMTP()
    smtp.connect(smtpsever)
    smtp.login(user,password)
    smtp.sendmail(sender,receiver.split(','),msg.as_string())
    smtp.quit()
    print(u'邮件发送成功')

if __name__ =="__main__":
    # testsuit()
    send_email()