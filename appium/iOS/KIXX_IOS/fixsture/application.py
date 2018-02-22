
from appium import webdriver
from General import config
from iOS.KIXX_IOS.fixsture.session import SessionHelper
from time import sleep

class Application:

    def __init__(self):
        desired_caps = config.ios_desired_caps()
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(20)
        self.session = SessionHelper(self)

    def allow(self):
        driver = self.driver
        allow = driver.find_elements_by_name("Allow")
        allow[0].click()

    def menu(self):
        icon_menu = self.driver.find_element_by_name("icon menu")
        icon_menu.click()

    def profile(self):
        avatar = self.driver.find_element_by_xpath("//XCUIElementTypeOther[1]/XCUIElementTypeImage")
        avatar.click()

    def vk_login(self):
        vk = self.driver.find_element_by_accessibility_id("ic vk")
        vk.click()
        sleep(8)
        self.driver.tap([(30, 235)])
        sleep(8)

    def destroy (self):
        self.driver.quit()



