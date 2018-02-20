import os
import unittest

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from iOS import iOSSwipeScroll

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class ContactsIosTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = '11.2'
        desired_caps['deviceName'] = 'iPhone 7'
        desired_caps['app'] = PATH('/Users/chechetkin/PycharmProjects/appium/app/BettingInsider.app')
        desired_caps['autoAcceptAlerts'] = "true"

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


    def tearDown(self):
        self.driver.quit()


    def test_kek(self):

        wait = WebDriverWait(self.driver, 20)

        for x in range(0, 4):
            point = iOSSwipeScroll.left(self)
            print(point[0], point[1], point[2], point[3])
            self.driver.swipe(point[0], point[1], point[2], point[3], 1000)

        allow = self.driver.find_elements_by_name("Allow")
        allow[0].click()

        tour5 = wait.until(
            EC.element_to_be_clickable((By.ID,
            "Continue without signing up")))
        tour5.click()

        profile = wait.until(
            EC.element_to_be_clickable((By.ID,
            "Profile")))
        profile.click()

        profile = wait.until(
            EC.element_to_be_clickable((By.ID,
            "Profile")))
        profile.click()

        profile = wait.until(
            EC.element_to_be_clickable((By.ID,
            "Profile")))
        profile.click()

        auth_mail = wait.until(
            EC.element_to_be_clickable((By.XPATH,
            "//XCUIElementTypeOther[4]/XCUIElementTypeOther[2]/XCUIElementTypeButton")))
        auth_mail.click()

        login = wait.until(
            EC.element_to_be_clickable((By.XPATH,
            "//XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeTextField")))
        login.send_keys("qwe@sports.ru")

        password = wait.until(
            EC.element_to_be_clickable((By.XPATH,
            "//XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther")))
        password.send_keys("password")

        sign_in = wait.until(
            EC.element_to_be_clickable((By.ID,
            "SIGN IN")))
        sign_in.click()

        # click_x = wait.until(
        #     EC.element_to_be_clickable((By.ID,
        #     "ic settings")))
        # click_x.click()

        settings = wait.until(
            EC.element_to_be_clickable((By.ID,
            "ic settings")))
        settings.click()

        click_xy = wait.until(
            EC.element_to_be_clickable((By.ID,
            "Get more funds to bet")))
        click_xy.click()

        point = iOSSwipeScroll.up(self)
        print(point[0], point[1], point[2], point[3])
        self.driver.swipe(point[0], point[1], point[2], point[3], 1000)

        logout = wait.until(
            EC.element_to_be_clickable((By.XPATH,
            "//XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[15]")))
        logout.click()

        back = wait.until(
            EC.element_to_be_clickable((By.ID,
            "Back")))
        back.click()












