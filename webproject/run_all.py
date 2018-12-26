#coding=utf-8
import unittest
import HTMLTestRunner
#将默认编码设置为utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#用例路径
casepath="F:\\Web_Auto\\webproject\\case"
rule="test*.py"
discover=unittest.defaultTestLoader.discover(start_dir=casepath,pattern=rule)
print (discover)


filename="F:\\Web_Auto\\webproject\\report\\"+"result.html"
fp=open(filename,'wb')
runner=HTMLTestRunner.HTMLTestRunner(stream=fp,
                                    title="自动化测试报告",
                                    description="禅道项目测试报告")
runner.run(discover)