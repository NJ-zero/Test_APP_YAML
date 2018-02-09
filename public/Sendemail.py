#coding=utf-8
#author='Shichao-Dong'

import time,os
import smtplib
import datetime
from public.readConfig import Readconfig
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.header import Header
from email.mime.multipart import MIMEMultipart


PATH = lambda p: os.path.abspath(
        os.path.join(os.path.dirname(__file__), p)
    )

conf = Readconfig()
sender = conf.getemailValue('sender')
receiver = conf.getemailValue('receiver')

class Email:

    def new_file(self):
        report_path = PATH("../results/")
        lists = os.listdir(report_path)
        lists.sort(key=lambda fn:os.path.getmtime(report_path+"\\"+fn))
        file_new=os.path.join(report_path,lists[-1])
        return file_new

    def email(self):
        f = open(self.new_file(),'rb')
        mail_body = f.read()
        f.close()

        #定义发件内容
        msg = MIMEText(mail_body,'html','utf-8')
        msg['Subject']=Header('外勤365客户端测试报告','utf-8')
        msg['from']=sender
        msg['to']=receiver

        return msg

