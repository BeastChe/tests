import unittest

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Android import AndroidSwipeScroll, auth
from General import config


class auth_onbording(unittest.TestCase):
    def setUp(self):
        desired_caps = config.android_desired_caps()
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


    def tearDown(self):
        self.driver.quit()

    def test_mail(self):
        wait = WebDriverWait(self.driver, 5)

        for x in range(0, 4):
            point = AndroidSwipeScroll.left(self)
            self.driver.swipe(point[0], point[1], point[2], point[3], 1000)

        auth.auth_mail(self)

        profile = wait.until(
            EC.element_to_be_clickable((By.ID,
                                        "com.tribuna.betting:id/action_profile")))
        profile.click()

        profile = wait.until(
            EC.element_to_be_clickable((By.ID,
                                        "com.tribuna.betting:id/action_profile")))
        profile.click()

        wait.until(EC.visibility_of_element_located((By.ID, "com.tribuna.betting:id/imgAvatar")))

    def test_signup(self):
        wait = WebDriverWait(self.driver, 5)

        for x in range(0, 4):
            point = AndroidSwipeScroll.left(self)
            self.driver.swipe(point[0], point[1], point[2], point[3], 1000)

        AuthEmail = wait.until(
            EC.element_to_be_clickable((By.ID,
                                        "com.tribuna.betting:id/btnOnBoardingEmail")))
        AuthEmail.click()

        auth.sign_up(self)

        profile = wait.until(
            EC.element_to_be_clickable((By.ID,
                                        "com.tribuna.betting:id/action_profile")))
        profile.click()

        profile = wait.until(
            EC.element_to_be_clickable((By.ID,
                                        "com.tribuna.betting:id/action_profile")))
        profile.click()

        wait.until(EC.visibility_of_element_located((By.ID, "com.tribuna.betting:id/imgAvatar")))

    def test_vk(self):
        wait = WebDriverWait(self.driver, 5)

        for x in range(0, 4):
            point = AndroidSwipeScroll.left(self)
            self.driver.swipe(point[0], point[1], point[2], point[3], 1000)

        auth.vk(self)

        profile = wait.until(
            EC.element_to_be_clickable((By.ID,
                                        "com.tribuna.betting:id/action_profile")))
        profile.click()

        profile = wait.until(
            EC.element_to_be_clickable((By.ID,
                                        "com.tribuna.betting:id/action_profile")))
        profile.click()

        wait.until(EC.visibility_of_element_located((By.ID, "com.tribuna.betting:id/imgAvatar")))

    def test_fb(self):
        wait = WebDriverWait(self.driver, 5)

        for x in range(0, 4):
            point = AndroidSwipeScroll.left(self)
            self.driver.swipe(point[0], point[1], point[2], point[3], 1000)

        auth.fb(self)

        profile = wait.until(
            EC.element_to_be_clickable((By.ID,
                                        "com.tribuna.betting:id/action_profile")))
        profile.click()

        profile = wait.until(
            EC.element_to_be_clickable((By.ID,
                                        "com.tribuna.betting:id/action_profile")))
        profile.click()

        wait.until(EC.visibility_of_element_located((By.ID, "com.tribuna.betting:id/imgAvatar")))

    def test_google(self):
        wait = WebDriverWait(self.driver, 5)

        for x in range(0, 4):
            point = AndroidSwipeScroll.left(self)
            self.driver.swipe(point[0], point[1], point[2], point[3], 1000)

        auth.google(self)

        profile = wait.until(
            EC.element_to_be_clickable((By.ID,
                                        "com.tribuna.betting:id/action_profile")))
        profile.click()

        profile = wait.until(
            EC.element_to_be_clickable((By.ID,
                                        "com.tribuna.betting:id/action_profile")))
        profile.click()

        wait.until(EC.visibility_of_element_located((By.ID, "com.tribuna.betting:id/imgAvatar")))

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(auth_onbording)
    unittest.TextTestRunner(verbosity=2).run(suite)

