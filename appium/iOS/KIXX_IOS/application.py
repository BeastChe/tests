
from appium import webdriver
from General import config
from iOS import iOSSwipeScroll


class Application:

    def __init__(self):
        desired_caps = config.ios_desired_caps()
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(20)

    def allow(self):
        driver = self.driver
        allow = driver.find_elements_by_name("Allow")
        allow[0].click()

    def logout(self):
        driver = self.driver
        logout = driver.find_element_by_accessibility_id("ic logout")
        logout.click()
        yes = driver.find_element_by_accessibility_id("YES")
        yes.click()

    def login_mail(self, login, password):
        driver = self.driver
        el1 = driver.find_element_by_accessibility_id("Log In")
        el1.click()
        el2 = driver.find_element_by_accessibility_id("ic mail")
        el2.click()
        el3 = driver.find_element_by_xpath("//XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]")
        el3.send_keys(login)
        el4 = driver.find_element_by_xpath("//XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[2]")
        el4.send_keys(password)
        el5 = driver.find_element_by_accessibility_id("SIGN IN")
        el5.click()

    def profile(self):
        avatar = self.driver.find_element_by_xpath("//XCUIElementTypeOther[1]/XCUIElementTypeImage")
        avatar.click()

    def destroy (self):
        self.driver.quit()

    def swipe (self, left, right, up, down):
        right = self.driver.swipe(iOSSwipeScroll.right, 300)
        left = self.driver.swipe(iOSSwipeScroll.left, 300)
        up = self.driver.swipe(iOSSwipeScroll.up, 300)
        down = self.driver.swipe(iOSSwipeScroll.down, 300)


