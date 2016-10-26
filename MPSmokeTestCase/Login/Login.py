# -*- coding: UTF-8 -*-
#!/usr/bin/python
import unittest
import os
from random import randint
from appium import webdriver#from selenium import webdriver
from time import sleep
import Params

class Login(unittest.TestCase):
    print '开始测试未登录的情况'
    def __init__(self,methodName):
        unittest.TestCase.__init__(self, methodName)

    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': '/Users/liteng/Desktop/MiaoPai.ipa',
                'platformName': 'iOS',
                'platformVersion': '9.3',
                'deviceName': 'iPhone 6s Plus',
                'udid': '4c0d9af518284810c7acd47c07cdc712424b19f0'

            })

    def test_loginweibo(self):
    	el_shoot = self.driver.find_element_by_accessibility_id("MPTTabarCapture")
    	el_shoot.click()
    	print"点击拍摄按钮弹出登录选项"
    	sleep(2)

    	el_weibologin = self.driver.find_element_by_accessibility_id("MPTLoginWeibo")
    	el_weibologin.click()
    	print"点击微博登录"
    	sleep(4)
        
        try:
        	el_jump = self.driver.find_element_by_accessibility_id("跳过")
    	    el_jump.click()
    	    print"跳过手机号绑定"
    	    sleep(3)
        except :
        	print"该账号已经绑定手机号"

        el_my = self.driver.find_element_by_accessibility_id("我的")
        el_my.click()
        print"进入我的界面"
        sleep(2)

        el_set = self.driver.find_element_by_accessibility_id("设置")
        el_set.click()
        print"进入设置界面"
        sleep(2)

        el_logout = self.driver.find_element_by_accessibility_id("退出当前账号")
        el_logout.click()
        print"点击退出当前账号"
        sleep(1)

        el_queren = self.driver.find_element_by_accessibility_id("确认")
        el_queren.click()
        print"退出当前账号"
        sleep(2)


    def tearDown(self):
    	self.driver.quit()
    	print"登录测试over"
	

def suite(self):
	suite = unittest.TestSuite()  
	suite.addTest(MPlogin('test_loginweibo'))  
	# suite.addTest(MPlogin('test_login2'))  
	# suite.addTest(MPlogin('test_login3'))
	# suite.addTest(MPlogin('test_login4'))

	runner = unittest.TextTestRunner()  
	runner.run(suite)