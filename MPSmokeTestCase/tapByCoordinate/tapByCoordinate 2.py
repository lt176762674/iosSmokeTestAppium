# -*- coding: UTF-8 -*-
#!/usr/bin/python
import unittest
import os
from random import randint
#from appium import webdriver#
from selenium import webdriver

from time import sleep

class tapByCoordinate(webdriver.Remote):
	def tapByCoordinate(self, element):
		location = element.location
		el_size = element.size
		return self.tap([(el_size['width'] / 2 + location['x'], el_size['height'] / 2 + location['y'],)])
