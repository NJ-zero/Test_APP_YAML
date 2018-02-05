## Test_APP_YAML
appium的UI测试，数据与用例分离，实现yaml管理用例

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