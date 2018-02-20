import unittest

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from General import config


class EbalTvouTelky(unittest.TestCase):
    def setUp(self):
        desired_caps = config.android_noreset_desired_caps()
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


    def tearDown(self):
        self.driver.quit()


    def test_kek(self):
        wait = WebDriverWait(self.driver, 20)


        el = wait.until(
            EC.element_to_be_clickable((By.ID,
            "com.tribuna.betting:id/etMessage")))
        el.click()

        el1 = wait.until(
            EC.element_to_be_clickable((By.ID,
                                        "com.tribuna.betting:id/imgSendMessage")))

        for x in range(0, 1000):

            # login = wait.until(
            #     EC.element_to_be_clickable((By.ID,
            #                                 "com.tribuna.betting:id/etMessage")))
            el.send_keys("Yurii Palich vseh ebal")

            el1.click()
