## Test_APP_YAML
appium的UI测试，数据与用例分离，实现yaml管理用例  

详细介绍，可见[个人主页](https://www.jianshu.com/p/00aff8435a92)

#### 环境说明
- windows
- appium 1.4(后来升级到1.6.4也没有问题)
- python2.7

#### yaml用例编写说明
````
testinfo:
    - id: cm001   
      title: 新增终端门店
      execute: 1          ----主要是用例名称，目前这三个参数没有用到，只是阅读方便
testcase:
    -
      element_info: 客户、com.fiberhome.waiqin365.client:id/cm_topbar_tv_right（来自Uiautomator识别出来）
      find_type:  text  id  xpath  ids
      operate_type: click、sendkeys、swipe_up、back、check        
      index: 0  find_type为ids时用到索引
      times： 上滑或者返回时用到
           
 ````          
#### 结构介绍
整体结果如图所示：

![image](https://github.com/NJ-zero/Test_APP_YAML/raw/master/framework.png)

- logs 用于存放日志
- page 存放每个模块的page，最小用例
- public 存放公共方法，如读取yaml、读取配置项、定位点击基础操作
- results 存放html测试结果和失败截图
- testcase 存放测试用例
- testyaml 存放yaml文件
- HTMLTestRunner.py 生成报告用
- runtest.py 运行所有测试用例用

#### 第一次优化
- 增加发送邮件功能
    - readconfig增加读取email参数方方法
    - config.ini增加邮件相关参数
    - Sendemail.py  新增发送邮件公共方法
    - runtest.py 增加发送邮件方法
- 修复bug
    - BaseOperate.py 中未定位到元素error日志显示问题，%s 加错位置
    - 失败截图，路径修改，screenshoot后加上filapic，要不然会直接生成在reults目录下
#### 0301第二次优化
- yaml文件operate_type增加check，用于校验
- 优化了定位元素的方法，增加等待时间
- BaseOperate.py 文件中，增加check的分支
- 判断元素是否存在，不存在时增加截图和日志