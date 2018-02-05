#coding=utf-8
#author='Shichao-Dong'

import sys
reload(sys)
sys.setdefaultencoding('utf8')
import yaml
import codecs



class getyaml:
    def __init__(self,path):
        self.path = path

    def getYaml(self):
        '''
        读取yaml文件
        :param path: 文件路径
        :return:
        '''
        try:
            f = open(self.path)
            data =yaml.load(f)
            f.close()
            return data
        except Exception:
            print(u"未找到yaml文件")

    def alldata(self):
        data =self.getYaml()
        return data

    def caselen(self):
        data = self.alldata()
        length = len(data['testcase'])
        return length

    def get_elementinfo(self,i):
        data = self.alldata()
        # print data['testcase'][i]['element_info']
        return data['testcase'][i]['element_info']

    def get_findtype(self,i):
        data = self.alldata()
        # print data['testcase'][i]['find_type']
        return data['testcase'][i]['find_type']

    def get_operate_type(self,i):
        data = self.alldata()
        # print data['testcase'][i]['operate_type']
        return data['testcase'][i]['operate_type']

    def get_index(self,i):
        data = self.alldata()
        if self.get_findtype(i)=='ids':
                    return data['testcase'][i]['index']
        else:
            pass

    def get_send_content(self,i):
        data = self.alldata()
        # print data['testcase'][i]['send_content']
        if self.get_operate_type(i) == 'send_keys':
            return data['testcase'][i]['send_content']
        else:
            pass

    def get_backtimes(self,i):
        data = self.alldata()
        if self.get_operate_type(i)=='back' or self.get_operate_type(i)=='swipe_up':
                    return data['testcase'][i]['times']
        else:
            pass

    def get_title(self):
        data = self.alldata()
        # print data['testinfo'][0]['title']
        return  data['testinfo'][0]['title']


# path = "../testyaml/cm/cm-001addcm.yaml"
# # print getyaml(path).alldata()
# # print getyaml(path).get_title()
# for i in range(getyaml(path).caselen()):
#     print getyaml(path).get_operate_type(i)
# #     print getyaml(path).get_elementinfo(i)
# #     print getyaml(path).get_findtype(i)
# #     print getyaml(path).get_send_content(i)
#     print getyaml(path).get_backtimes(i)
# #     index =getyaml(path).get_index(i)
# #     print index