#coding=utf-8
#author='Shichao-Dong'
import os,time

now=time.strftime("%y-%m-%d-%H-%M-%S")
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
dirpath = PATH(r"./results/waiqin365-")


filename=dirpath + now +'result.html'
print dirpath,filename