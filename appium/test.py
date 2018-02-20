import os
import unittest

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Android import AndroidSwipeScroll

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)



class ContactsAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6'
        desired_caps['deviceName'] = 'Huawei'
        desired_caps['app'] = PATH ('/Users/chechetkin/PycharmProjects/appium/app/Betting Insider_com.tribuna.betting.apk')
        desired_caps['appWaitActivity'] = '*'
        desired_caps['noReset'] = 'true'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


    def tearDown(self):
        self.driver.quit()

    def test_kek(self):

        wait = WebDriverWait(self.driver, 20)

        # for x in range(0, 4):
        #     point = AndroidSwipeScroll.left(self)
        #     print(point[0], point[1], point[2], point[3])
        #     self.driver.swipe(point[0], point[1], point[2], point[3], 1000)
        #
        # tour5 = wait.until(
        #      EC.element_to_be_clickable((By.ID,
        #      "com.tribuna.betting:id/txtContinue")))
        # tour5.click()
        #
        # profile = wait.until(
        #     EC.element_to_be_clickable((By.ID,
        #     "com.tribuna.betting:id/action_profile")))
        # profile.click()
        #
        # profile = wait.until(
        #     EC.element_to_be_clickable((By.ID,
        #     "com.tribuna.betting:id/action_profile")))
        # profile.click()
        #
        # AuthEmail = wait.until(
        #     EC.element_to_be_clickable((By.ID,
        #     "com.tribuna.betting:id/btnAuthEmail")))
        # AuthEmail.click()
        #
        # login = wait.until(
        #     EC.element_to_be_clickable((By.ID,
        #     "com.tribuna.betting:id/etLogin")))
        # login.send_keys("qwe@sports.ru")
        #
        # password = wait.until(
        #     EC.element_to_be_clickable((By.ID,
        #     "com.tribuna.betting:id/etPassword")))
        # password.send_keys("password")
        #
        # signIn = wait.until(
        #     EC.element_to_be_clickable((By.ID,
        #     "com.tribuna.betting:id/btnSignIn")))
        # signIn.click()
        #
        # clickXyi = wait.until(
        #     EC.element_to_be_clickable((By.ID,
        #     "com.tribuna.betting:id/imgAvatar")))
        # clickXyi.click()
        #
        # wait_profile = wait.until(
        #     EC.element_to_be_clickable((By.ID,
        #     "com.tribuna.betting:id/imgAvatar")))
        #
        # settings = wait.until(
        #     EC.element_to_be_clickable((By.ID,
        #     "com.tribuna.betting:id/miSettings")))
        # settings.click()
        #
        # clickXyi = wait.until(
        #     EC.element_to_be_clickable((By.ID,
        #     "com.tribuna.betting:id/scNewSubscribers")))
        # clickXyi.click()
        #
        # point = AndroidSwipeScroll.up(self)
        # print(point[0], point[1], point[2], point[3])
        # self.driver.swipe(point[0], point[1], point[2], point[3], 1000)
        #
        # logout = wait.until(
        #     EC.element_to_be_clickable((By.ID,
        #     "com.tribuna.betting:id/cvExit")))
        # logout.click()
        #
        # back = wait.until(
        #     EC.element_to_be_clickable((By.XPATH,
        #     "//android.widget.ImageButton")))
        # back.click()

        # Sign_up

        #Пока это краш

        # sign_up = wait.until(
        #     EC.element_to_be_clickable((By.ID,
        #        "com.tribuna.betting:id/txtSignUp")))
        # sign_up.click()
        #
        # mail = wait.until(
        #     EC.element_to_be_clickable((By.ID,
        #     "com.tribuna.betting:id/etEmail")))
        # mail.send_keys(rnd_mail.generate_random_emails())
        #
        # password = wait.until(
        #     EC.element_to_be_clickable((By.ID,
        #     "com.tribuna.betting:id/etPassword")))
        # password.send_keys("q12345")
        #
        # repeat_password = wait.until(
        #     EC.element_to_be_clickable((By.ID,
        #     "com.tribuna.betting:id/etPasswordConfirm")))
        # repeat_password.send_keys("q12345")
        #
        # login = wait.until(
        #     EC.element_to_be_clickable((By.ID,
        #     "com.tribuna.betting:id/btnSignUp")))
        # login.click()
        #
        # wait_profile = wait.until(
        #     EC.element_to_be_clickable((By.ID,
        #     "com.tribuna.betting:id/imgAvatar")))
        #
        # settings = wait.until(
        #     EC.element_to_be_clickable((By.ID,
        #     "com.tribuna.betting:id/miSettings")))
        # settings.click()
        #
        # point = AndroidSwipeScroll.up(self)
        # print(point[0], point[1], point[2], point[3])
        # self.driver.swipe(point[0], point[1], point[2], point[3], 1000)
        #
        # logout = wait.until(
        #     EC.element_to_be_clickable((By.ID,
        #     "com.tribuna.betting:id/cvExit")))
        # logout.click()
        #
        # back = wait.until(
        #     EC.element_to_be_clickable((By.XPATH,
        #     "//android.widget.ImageButton")))
        # back.click()

        #VK

        profile = wait.until(
            EC.element_to_be_clickable((By.ID,
            "com.tribuna.betting:id/action_profile")))
        profile.click()

        authVK = wait.until(
            EC.element_to_be_clickable((By.ID,
            "com.tribuna.betting:id/btnAuthVk")))
        authVK.click()



        try:
            print('trololo')

            wait.until(EC.element_to_be_clickable((By.XPATH, "//android.view.View/android.view.View/android.view.View[6]")))
            #self.driver.find_element_by_xpath("//android.view.View/android.view.View/android.view.View[6]")
            print('kek')
            login = wait.until(
                EC.element_to_be_clickable((By.XPATH,
                "//android.view.View/android.view.View/android.view.View[6]")))
            login.click()

        except:
            login = wait.until(
                EC.element_to_be_clickable((By.XPATH,
                "//android.widget.ListView[1]/android.view.View[2]/android.widget.EditText")))
            login.send_keys("79645767263")

            password = wait.until(
                EC.element_to_be_clickable((By.XPATH,
                "//android.widget.ListView[2]/android.view.View[2]/android.widget.EditText")))
            password.send_keys("qwersalam")

            login = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME,
                "android.widget.Button")))
            login.click()

            allow = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME,
                "android.widget.Button")))
            allow.click()

        wait_profile = wait.until(
            EC.element_to_be_clickable((By.ID,
            "com.tribuna.betting:id/imgAvatar")))

        settings = wait.until(
            EC.element_to_be_clickable((By.ID,
            "com.tribuna.betting:id/miSettings")))
        settings.click()

        point = AndroidSwipeScroll.up(self)
        print(point[0], point[1], point[2], point[3])
        self.driver.swipe(point[0], point[1], point[2], point[3], 1000)

        logout = wait.until(
            EC.element_to_be_clickable((By.ID,
            "com.tribuna.betting:id/cvExit")))
        logout.click()

        back = wait.until(
            EC.element_to_be_clickable((By.XPATH,
            "//android.widget.ImageButton")))
        back.click()

        #Facebook

        authFB = wait.until(
            EC.element_to_be_clickable((By.ID,
            "com.tribuna.betting:id/btnAuthFacebook")))
        authFB.click()

        login = wait.until(
            EC.element_to_be_clickable((By.XPATH,
            "//android.view.View[3]/android.widget.EditText[1]")))
        login.send_keys("79691487427")

        password = wait.until(
            EC.element_to_be_clickable((By.XPATH,
            "//android.view.View[3]/android.widget.EditText[2]")))
        password.send_keys("habib1488f")

        login = wait.until(
            EC.element_to_be_clickable((By.ID,
            "Log In")))
        login.click()

        allow = wait.until(
            EC.element_to_be_clickable((By.ID,
            "Продолжить")))
        allow.click()

        wait_profile = wait.until(
            EC.element_to_be_clickable((By.ID,
            "com.tribuna.betting:id/imgAvatar")))

        settings = wait.until(
            EC.element_to_be_clickable((By.ID,
            "com.tribuna.betting:id/miSettings")))
        settings.click()

        point = AndroidSwipeScroll.up(self)
        print(point[0], point[1], point[2], point[3])
        self.driver.swipe(point[0], point[1], point[2], point[3], 1000)

        logout = wait.until(
            EC.element_to_be_clickable((By.ID,
            "com.tribuna.betting:id/cvExit")))
        logout.click()

        back = wait.until(
            EC.element_to_be_clickable((By.XPATH,
            "//android.widget.ImageButton")))
        back.click()

        # Google

        authG = wait.until(
            EC.element_to_be_clickable((By.ID,
            "com.tribuna.betting:id/btnAuthGoogle")))
        authG.click()

        # login = wait.until(
        #     EC.element_to_be_clickable((By.ID,
        #     "/Email or phone")))
        # login.send_keys("testforappium@gmail.com")
        #
        # next = wait.until(
        #     EC.element_to_be_clickable((By.ID,
        #     "NEXT")))
        # next.click()
        #
        # password = wait.until(
        #     EC.element_to_be_clickable((By.ID,
        #     "Password")))
        # password.send_keys("qw12345x")
        #
        # next = wait.until(
        #     EC.element_to_be_clickable((By.ID,
        #     "NEXT")))
        # next.click()
        #
        # next = wait.until(
        #     EC.element_to_be_clickable((By.ID,
        #     "ACCEPT")))
        # next.click()
        #
        # login = wait.until(
        #     EC.element_to_be_clickable((By.ID,
        #     "com.google.android.gms:id/suw_navbar_next")))
        # login.click()
        #
        #
        # allow = wait.until(
        #     EC.element_to_be_clickable((By.ID,
        #     "com.google.android.gms:id/accept_button")))
        # allow.click()

        name = wait.until(
            EC.element_to_be_clickable((By.XPATH,
            "//android.widget.LinearLayout[1]/android.widget.LinearLayout")))
        name.click()

        wait_profile = wait.until(
            EC.element_to_be_clickable((By.ID,
            "com.tribuna.betting:id/imgAvatar")))

        settings = wait.until(
            EC.element_to_be_clickable((By.ID,
            "com.tribuna.betting:id/miSettings")))
        settings.click()

        point = AndroidSwipeScroll.up(self)
        print(point[0], point[1], point[2], point[3])
        self.driver.swipe(point[0], point[1], point[2], point[3], 1000)

        logout = wait.until(
            EC.element_to_be_clickable((By.ID,
            "com.tribuna.betting:id/cvExit")))
        logout.click()

        back = wait.until(
            EC.element_to_be_clickable((By.XPATH,
            "//android.widget.ImageButton")))
        back.click()