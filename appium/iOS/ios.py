from appium import webdriver
import unittest
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
import time


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class ContactsIosTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = '11.1'
        desired_caps['deviceName'] = 'iPhone 7'
        desired_caps['app'] = PATH('/Users/chechetkin/PycharmProjects/appium/app/Kixx.app')
        desired_caps['autoAcceptAlerts'] = "true"

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)




    def tearDown(self):
        self.driver.quit()


    def test_kek(self):

        wait = WebDriverWait(self.driver, 20)

        allow = self.driver.find_elements_by_name("Allow")
        allow[0].click()

        logIn = wait.until(
            EC.element_to_be_clickable((By.ID,
            "Log In")))
        logIn.click()

        mail = wait.until(
            EC.element_to_be_clickable((By.ID,
            "ic mail")))
        mail.click()

        login = wait.until(
            EC.element_to_be_clickable((By.XPATH,
            "//XCUIElementTypeApplication[@name=\"Kixx\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]")))
        login.send_keys("chechetkin@sports.ru")

        password = wait.until(
            EC.element_to_be_clickable((By.XPATH,
            "//XCUIElementTypeApplication[@name=\"Kixx\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[2]")))
        password.send_keys("Qw641025")

        signIn = wait.until(
            EC.element_to_be_clickable((By.ID,
        "SIGN IN")))
        signIn.click()



        time.sleep(5)
        print ("go")

        window_size = self.driver.get_window_size()
        max_width = window_size["width"] - 1
        max_height = window_size["height"] - 1

        startX = 1
        startY = round(max_height/2)
        endX = round(max_width - 20)
        endY = 0

        print(startX,startY,endX,endY)


        self.driver.swipe(startX, startY, endX, endY, 1000)


        iconAdd = wait.until(
            EC.element_to_be_clickable((By.ID,
            "icon add")))
        iconAdd.click()



        #TouchAction(self.driver).press(x=180, y=560).move_to(x=-1, y=-280).release().perform()






