
from time import sleep





from selenium.webdriver.common.action_chains import ActionChains

class SessionHelper:

    def __init__ (self,app):
        self.app = app


    def login_mail(self, login, password):
        driver = self.app.driver
        driver.find_element_by_accessibility_id("ic mail").click()
        driver.find_element_by_xpath("//XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]").send_keys(login)
        driver.find_element_by_xpath("//XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[2]").send_keys(password)
        driver.find_element_by_accessibility_id("SIGN IN").click()
        sleep(2) # какой-то микробаг, приложение зависает если сразу в меню заходить


    def vk_login(self, login, password):
        driver = self.app.driver
        driver.find_element_by_accessibility_id("ic vk").click()
        try:
            driver.find_element_by_class_name("XCUIElementTypeTextField").send_keys(login)
            driver.find_element_by_class_name("XCUIElementTypeSecureTextField").send_keys(password)
            driver.find_element_by_accessibility_id("Log in").click()
            driver.find_element_by_accessibility_id("Allow").click()
        except:
            pass


    def fb_login(self, login, password):
        driver = self.app.driver
        driver.find_element_by_accessibility_id("ic fb").click()
        try:
            driver.find_element_by_class_name("XCUIElementTypeTextField").send_keys(login)
            driver.find_element_by_class_name("XCUIElementTypeSecureTextField").click()
            driver.find_element_by_class_name("XCUIElementTypeSecureTextField").send_keys(password)
            driver.find_element_by_accessibility_id("Log In").click()
            driver.find_element_by_class_name("XCUIElementTypeButton").click()
            driver.find_element_by_accessibility_id("Продолжить").click()

        except:
            driver.find_element_by_accessibility_id("Продолжить").click()

    def tw_login(self, login, password):
        driver = self.app.driver
        driver.find_element_by_accessibility_id("ic tw").click()
        driver.find_element_by_class_name("XCUIElementTypeTextField").send_keys(login)
        driver.find_element_by_class_name("XCUIElementTypeSecureTextField").click()
        driver.find_element_by_class_name("XCUIElementTypeSecureTextField").send_keys(password)
        driver.find_element_by_accessibility_id("Войти").click()



    def logout(self):
        driver = self.app.driver
        logout = driver.find_element_by_accessibility_id("ic logout")
        logout.click()
        yes = driver.find_element_by_accessibility_id("YES")
        yes.click()