import unittest

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Android import auth
from General import config


class popup(unittest.TestCase):
    def setUp(self):
        desired_caps = config.android_noreset_desired_caps()
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


    def tearDown(self):
        self.driver.quit()

    def test_popup(self):

        wait = WebDriverWait(self.driver, 20)

        rebet = wait.until(
            EC.element_to_be_clickable((By.ID,
            "com.tribuna.betting:id/ltTourForecast")))
        rebet.click()

        auth.auth_mail(self)

        profile = wait.until(
            EC.element_to_be_clickable((By.ID,
            "com.tribuna.betting:id/action_profile")))
        profile.click()

        auth.step_logout(self)

        predictions = wait.until(
            EC.element_to_be_clickable((By.ID,
            "com.tribuna.betting:id/action_tips")))
        predictions.click()

        rebet = wait.until(
            EC.element_to_be_clickable((By.ID,
            "com.tribuna.betting:id/ltTourForecast")))
        rebet.click()


        auth.sign_up(self)

        profile = wait.until(
            EC.element_to_be_clickable((By.ID,
            "com.tribuna.betting:id/action_profile")))
        profile.click()


        auth.step_logout(self)

        predictions = wait.until(
            EC.element_to_be_clickable((By.ID,
            "com.tribuna.betting:id/action_tips")))
        predictions.click()

        rebet = wait.until(
            EC.element_to_be_clickable((By.ID,
            "com.tribuna.betting:id/ltTourForecast")))
        rebet.click()

        auth.vk(self)

        profile = wait.until(
            EC.element_to_be_clickable((By.ID,
            "com.tribuna.betting:id/action_profile")))
        profile.click()

        auth.step_logout(self)

        predictions = wait.until(
            EC.element_to_be_clickable((By.ID,
            "com.tribuna.betting:id/action_tips")))
        predictions.click()

        rebet = wait.until(
            EC.element_to_be_clickable((By.ID,
            "com.tribuna.betting:id/ltTourForecast")))
        rebet.click()



        auth.fb(self)

        profile = wait.until(
            EC.element_to_be_clickable((By.ID,
            "com.tribuna.betting:id/action_profile")))
        profile.click()
        auth.step_logout(self)

        predictions = wait.until(
            EC.element_to_be_clickable((By.ID,
            "com.tribuna.betting:id/action_tips")))
        predictions.click()

        rebet = wait.until(
            EC.element_to_be_clickable((By.ID,
            "com.tribuna.betting:id/ltTourForecast")))
        rebet.click()

        auth.google(self)

        profile = wait.until(
            EC.element_to_be_clickable((By.ID,
            "com.tribuna.betting:id/action_profile")))
        profile.click()

        auth.step_logout(self)

        predictions = wait.until(
            EC.element_to_be_clickable((By.ID,
                                        "com.tribuna.betting:id/action_tips")))
        predictions.click()

        rebet = wait.until(
            EC.element_to_be_clickable((By.ID,
                                        "com.tribuna.betting:id/ltTourForecast")))
        rebet.click()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(popup)
    unittest.TextTestRunner(verbosity=2).run(suite)
