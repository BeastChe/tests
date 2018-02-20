import unittest

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Android import auth
from General import config


class auth_profile(unittest.TestCase):
    def setUp(self):
        desired_caps = config.android_noreset_desired_caps()
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


    def tearDown(self):
        self.driver.quit()


    def test_auth(self):

        wait = WebDriverWait(self.driver, 5)

        profile = wait.until(
            EC.element_to_be_clickable((By.ID,
            "com.tribuna.betting:id/action_profile")))
        profile.click()


        auth.auth_mail(self)
        wait.until(EC.visibility_of_element_located((By.ID, "com.tribuna.betting:id/imgAvatar")))
        auth.step_logout(self)




        auth.sign_up(self)
        wait.until(EC.visibility_of_element_located((By.ID, "com.tribuna.betting:id/imgAvatar")))
        auth.step_logout(self)


        auth.vk(self)
        wait.until(EC.visibility_of_element_located((By.ID, "com.tribuna.betting:id/imgAvatar")))
        auth.step_logout(self)



        auth.fb(self)
        wait.until(EC.visibility_of_element_located((By.ID, "com.tribuna.betting:id/imgAvatar")))
        auth.step_logout(self)



        auth.google(self)
        wait.until(EC.visibility_of_element_located((By.ID, "com.tribuna.betting:id/imgAvatar")))
        auth.step_logout(self)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(auth_profile)
    unittest.TextTestRunner(verbosity=2).run(suite)