#coding=utf-8
#author='Shichao-Dong'

import os
import collections

def all_file_path(root_directory, extension_name):
    '''
    遍历目录
    :param root_directory: 目录
    :param extension_name: 文件扩展名
    :return:
    '''
    file_dic = collections.OrderedDict()
    for parent, dirnames, filenames in os.walk(root_directory):
        for filename in filenames:
            if 'filter' not in filename:
                if filename.endswith(extension_name):
                    path = os.path.join(parent, filename).replace('\\', '/')
                    file_dic[filename] = path
    return file_dic


if __name__ == '__main__':
    for k, v in all_file_path('../testyaml', '.yaml').items():
        print k,v

    for parent, dirnames, filenames in os.walk('../testyaml'):
        print parent
        for dirname in dirnames:
            print dirname
