
from appium import webdriver
from General import config
from iOS.KIXX_IOS.fixture.session import SessionHelper
from iOS.KIXX_IOS.fixture.user_data import UserHelper




class Application:

    def __init__(self):
        desired_caps = config.ios_desired_caps()
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)
        self.session = SessionHelper(self)
        self.user_data = UserHelper(self)

    def is_valid (self):
        driver = self.driver
        try:
            if driver.find_element_by_accessibility_id("Log In").is_displayed() and driver.find_element_by_accessibility_id("GET STARTED").is_displayed():
                return True

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

    def select_your_tournament(self):
        driver = self.driver
        driver.find_element_by_accessibility_id("Back").click()  # Чтобы не добавлять шаг клик на логин везде, я лучше в этом тесте вернусь назад
        driver.find_element_by_xpath("//XCUIElementTypeButton[2]").click()


    #ТУР
    def pass_tour(self):
        driver = self.driver
        driver.find_element_by_accessibility_id("DO IT FOR ME").click()
        driver.find_element_by_accessibility_id("GOT IT").click()
        driver.find_element_by_accessibility_id("GOT IT").click()
        driver.find_element_by_accessibility_id("PICK FOR ME").click()
        driver.find_element_by_accessibility_id("GOT IT").click()
        driver.find_element_by_accessibility_id("DO IT FOR ME").click()
        driver.find_element_by_accessibility_id("PICK FOR ME").click()
        driver.find_element_by_accessibility_id("DO IT FOR ME").click()
        driver.find_element_by_xpath("//XCUIElementTypeOther[2]/XCUIElementTypeButton").click()
        driver.find_element_by_accessibility_id("DO IT FOR ME").click()
        driver.find_element_by_accessibility_id("PICK FOR ME").click()
        driver.find_element_by_accessibility_id("ic check big").click()

    def lobby_loaded (self):
        contests = self.driver.find_element_by_accessibility_id("Contests")
        league_card = self.driver.find_element_by_xpath("//XCUIElementTypeCell[3]")
        if contests.is_displayed() and league_card.is_displayed():
            return True

    def destroy (self):
        self.driver.quit()



