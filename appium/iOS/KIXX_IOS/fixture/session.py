
from time import sleep


class SessionHelper:

    def __init__ (self,app):
        self.app = app


    def first_run(self):
        driver = self.app.driver
        allow = driver.find_elements_by_name("Allow")
        allow[0].click()
        driver.find_element_by_accessibility_id("Log In").click()

    def login_mail(self, login, password):
        driver = self.app.driver
        driver.find_element_by_accessibility_id("ic mail").click()
        driver.find_element_by_xpath("//XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]").send_keys(login)
        driver.find_element_by_xpath("//XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[2]").send_keys(password)
        driver.find_element_by_accessibility_id("SIGN IN").click()
        sleep(2)  # какой-то микробаг, приложение зависает если сразу в меню заходить за польхователя с евро

    def signup_mail(self, name, email, password):
        driver = self.app.driver
        driver.find_element_by_accessibility_id("Your name").send_keys(name)
        driver.find_element_by_accessibility_id("Your email").send_keys(email)
        driver.find_element_by_accessibility_id("Password").send_keys(password)
        driver.find_element_by_accessibility_id("JOIN FOR FREE").click()

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

    def logout_from_lobby (self):
        driver = self.app.driver
        driver.find_element_by_name("icon menu").click()
        driver.find_element_by_xpath("//XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable/XCUIElementTypeCell[1]").click()
        driver.find_element_by_accessibility_id("ic logout").click()
        driver.find_element_by_accessibility_id("YES").click()
