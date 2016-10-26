# -*- coding: UTF-8 -*-
#!/usr/bin/python
import unittest
import os
from random import randint
from appium import webdriver#from selenium import webdriver

from time import sleep



class StartAPP(unittest.TestCase):
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
        
    # def tapByCoordinate(self, element):
    #     location = element.location
    #     el_size = element.size
    #     return self.tap([(el_size['width'] / 2 + location['x'], el_size['height'] / 2 + location['y'],)])
    

    def test_01(self):
        try:
            el_hao = self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[7]/UIAAlert[1]/UIACollectionView[1]/UIACollectionCell[2]")
            el_hao.click()
            print "允许秒拍发送通知"
            sleep(2)

            el_baobao = self.driver.find_element_by_accessibility_id('跳过')
            el_baobao.click()
            print "跳过兴趣选择"
            sleep(2)
        except:
            pass
    
    def test_02(self):
        el_guanzhu = self.driver.find_element_by_accessibility_id("关注")
        el_guanzhu.click()
        print("进入关注界面")
        sleep(3)

        try:
            el_hao = self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[7]/UIAAlert[1]/UIACollectionView[1]/UIACollectionCell[2]")
            el_hao.click()
            print "允许秒拍发送通知"
            sleep(2)

            el_baobao = self.driver.find_element_by_accessibility_id('跳过')
            el_baobao.click()
            print "跳过兴趣选择"
            sleep(2)
        except:
            pass
        
        el_tongcheng = self.driver.find_element_by_accessibility_id("同城")
        el_tongcheng.click()
        print"进入同城界面"
        sleep(3)

        try:
            el_hao = self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[7]/UIAAlert[1]/UIACollectionView[1]/UIACollectionCell[2]")
            el_hao.click()
            print "允许秒拍发送通知"
            sleep(2)

            el_baobao = self.driver.find_element_by_accessibility_id('跳过')
            el_baobao.click()
            print "跳过兴趣选择"
            sleep(2)
        except:
            pass

        # el_ChooseType = self.driver.find_element_by_accessibility_id("MPTHome+")
        # el_ChooseType.click()
        # print"展开频道选择面板"
        # sleep(3)

        el_star = self.driver.find_element_by_accessibility_id("明星")
        el_star.click()
        print"选择明星频道"
        sleep(3)

        el_hot = self.driver.find_element_by_accessibility_id("热榜")
        el_hot.click()
        print"进入热榜界面"
        sleep(3)

        el_find = self.driver.find_element_by_accessibility_id("发现")
        el_find.click()
        print"进入发现界面"
        sleep(3)

        el_zhuixing = self.driver.find_element_by_accessibility_id("追星")
        el_zhuixing.click()
        print"进入追星界面"
        sleep(3)
        
        #以下方法报错，该按钮不可点击
        # el_back01 = self.driver.find_element_by_accessibility_id("返回")
        # el_back01.tapByCoordinate()
        # print"回到发现界面"
        # sleep(2)

        #以下方法报错，keyerror：‘y’
        # el_all = self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[2]")
        # location = el_all.location
        # size = el_all.size
        # self.driver.swipe(start_x=location['x'], start_y=size['y']/2, end_x=size['x'], end_y=size['y']/2, duration=800)
        
        #以下方法可用
        el_back01 = self.driver.find_element_by_accessibility_id("返回")
        location = el_back01.location
        el_size = el_back01.size
        self.driver.tap([(el_size['width'] / 2 + location['x'], el_size['height'] / 2 + location['y'],)])
        print"回到发现界面"
        sleep(2)

        # el_back01 = self.driver.find_element_by_accessibility_id("返回")
        # self.tapByCoordinate(el_back01)

        #以下方法可用
        # self.driver.swipe(0,100,250,100,500)
        # print"左滑回到发现界面"
        # sleep(2)

        # el_back01 = self.driver.find_element_by_accessibility_id("返回")
        # action = TouchAction(driver)
        # action.press(element=el, x=10, y=10).release().perform()
        # print"点击返回按钮"
        


        el_jiaoyou = self.driver.find_element_by_accessibility_id("交友")
        el_jiaoyou.click()
        print"进入交友界面"
        sleep(3)
        el_back02 = self.driver.find_element_by_accessibility_id("返回")
        location02 = el_back02.location
        el_size02 = el_back02.size
        self.driver.tap([(el_size02['width'] / 2 + location02['x'], el_size02['height'] / 2 + location02['y'],)])


    def test_UnloginMy(self):
        el_my = self.driver.find_element_by_accessibility_id("我的")
        el_my.click()
        print"进入我的界面"
        sleep(2)

        el_guanzhu = self.driver.find_element_by_accessibility_id("关注")
        el_guanzhu.click()
        print"进入关注界面"
        sleep(3)
        self.driver.swipe(0,100,250,100,500)
        print"左滑回到发现界面"
        sleep(2)

        el_jrts = self.driver.find_element_by_accessibility_id("今日推送")
        el_jrts.click()
        print"进入今日推送详情界面"
        sleep(2)
        self.driver.swipe(0,100,250,100,500)
        print"左滑回到发现界面"
        sleep(2)

        el_Unwifi = self.driver.find_element_by_accessibility_id("免流量视频")
        el_Unwifi.click()
        print"进入免流量视频界面"
        sleep(3)
        self.driver.swipe(0,100,250,100,500)
        print"左滑回到发现界面"
        sleep(2)

        el_tcbs = self.driver.find_element_by_accessibility_id("吐槽不爽")
        el_tcbs.click()
        print"进入吐槽不爽界面"
        sleep(3)
        self.driver.swipe(0,100,250,100,500)
        print"左滑回到发现界面"
        sleep(2)

        el_sz = self.driver.find_element_by_accessibility_id("设置")
        el_sz.click()
        print"进入设置界面"
        sleep(3)
        self.driver.swipe(0,100,250,100,500)
        print"左滑回到发现界面"
        sleep(2)

    
    

    def tearDown(self):
        self.driver.quit()
        print "over"
        

# if __name__ == '__main__':
#     # suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
#     # unittest.TextTestRunner(verbosity=2).run(suite)
#     unittest.main()

def suite(self):
    suite = unittest.TestSuite() 
    suite.addTest(StartAPP("test_01"))
    suite.addTest(StartAPP("test_02"))
    suite.addTest(StartAPP("test_UnloginMy"))

    runner = unittest.TextTestRunner()
    runner.run(suite)