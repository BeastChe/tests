
from appium import webdriver
from General import config
from iOS.KIXX_IOS.fixture.session import SessionHelper
from iOS.KIXX_IOS.fixture.user import UserHelper



class Application:

    def __init__(self):
        desired_caps = config.ios_desired_caps()
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)
        self.session = SessionHelper(self)
        self.user = UserHelper(self)

    def is_valid (self):
        try:
            0==1
        except:
            return False

    def allow(self):
        driver = self.driver
        allow = driver.find_elements_by_name("Allow")
        allow[0].click()

    def login(self):
        driver = self.driver
        driver.find_element_by_accessibility_id("Log In").click()


    def menu(self):
        icon_menu = self.driver.find_element_by_name("icon menu")
        icon_menu.click()

    def click_profile(self):
        self.driver.find_element_by_xpath("//XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable/XCUIElementTypeCell[1]").click()

    def get_started(self):
        self.driver.find_element_by_accessibility_id("GET STARTED").click()

    def destroy (self):
        self.driver.quit()



