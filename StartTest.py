# -*- coding: UTF-8 -*-
#!/usr/bin/python
import unittest
import sys
import os

#print sys.path
curDir = sys.path[0]
sys.path.append(curDir + '/MPSmokeTestCase/StartAPP')
sys.path.append(curDir + "MPSmokeTestCase/Login")

import StartAPP
import Login
# /Users/liteng/Desktop/MP_SmokeTest_iOS/MPSmokeTestCase/StartAPP
# sys.path.append(curDir + '\\MPSmokeTestCase\\Discovery')
# sys.path.append(curDir + '\\MPSmokeTestCase\\hot')
# sys.path.append(curDir + '\\MPSmokeTestCase\\Login')
# sys.path.append(curDir + '\\MPSmokeTestCase\\Shoot')
# sys.path.append(curDir + '\\MPSmokeTestCase\\Me')


# import MPlogin
# import MPshoot
# import MPsetting
# import MPTest


# MPlogin.suite("0")
# MPshoot.suite("0")
# #MPTest.suite("0")
# MPsetting.suite("0")

StartAPP.suite("0")
Login.suite("0")
