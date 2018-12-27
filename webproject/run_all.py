#coding=utf-8
import unittest
import HTMLTestRunner
#将默认编码设置为utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#用例路径
casepath="F:\\github\\Web_Auto\\webproject\\case"
rule="test*.py"
discover=unittest.defaultTestLoader.discover(start_dir=casepath,pattern=rule)
print (discover)


filename="F:\\github\\Web_Auto\\webproject\\report\\"+"result.html"
fp=file(filename,'wb')
runner=HTMLTestRunner.HTMLTestRunner(stream=fp,
                                    title='自动化测试报告',
                                    description='禅道项目测试报告')
runner.run(discover)