import random
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



    def pass_tour(self):
        driver = self.driver

# тут я хочу изобрести велосипед чтобы можно было рандомно выбирать кликать на текст или выполнять действие, нужно сделать это в этом тысячелетии

        step1 = [
                """driver.find_element_by_accessibility_id("DO IT FOR ME").click()""",
                """driver.find_element_by_accessibility_id("Tap position F to pick a forward").click()"""
                ]

        step2 = [
                """driver.find_element_by_accessibility_id("GOT IT").click()""",
                """driver.find_element_by_accessibility_id("AVG means player’s average points in last 10 games").click()"""
                ]

        step3 = [
                """driver.find_element_by_accessibility_id("GOT IT").click()""",
                """driver.find_element_by_accessibility_id("The players are rated from 1 to 3 stars. Your budget is restricted").click()"""
                ]

        step4 = [
                """driver.find_element_by_accessibility_id("PICK FOR ME").click()""",
                """driver.find_element_by_accessibility_id("plus").click()"""
                # --ИМЯ ИГРОКА-- is a really good forward. Pick him now!
                ]

        # step5 = [
        #         driver.find_element_by_accessibility_id("GOT IT").click(),
        #         driver.find_element_by_accessibility_id("Your team grows! And your budget is declining").click()
        #         ]
        #
        # step6 = [
        #         driver.find_element_by_accessibility_id("DO IT FOR ME").click(),
        #         driver.find_element_by_accessibility_id("Midfielder").click(),
        #         driver.find_element_by_accessibility_id("Tap to see other positions").click()
        #         ]
        #
        # step7 = [
        #         driver.find_element_by_accessibility_id("PICK FOR ME").click(),
        #         driver.find_element_by_accessibility_id("plus").click()
        #         ]
        #
        # step8 = [
        #         driver.find_element_by_accessibility_id("DO IT FOR ME").click(),
        #         driver.find_element_by_accessibility_id("Back").click(),
        #         driver.find_element_by_accessibility_id("Tap to see your team and vacant positions").click()
        #         ]
        #
        # step9 = [
        #         driver.find_element_by_xpath("//XCUIElementTypeOther[2]/XCUIElementTypeButton").click()
        #         ]
        #
        # step10 = [
        #         driver.find_element_by_accessibility_id("DO IT FOR ME").click()
        #         #"You have --кол-во звёзд-- stars for --кол-во игроков-- players.Use Cost filter to see cheaper ones"
        #         ]
        #
        # step11 = [
        #         driver.find_element_by_accessibility_id("PICK FOR ME").click()
        #         ]
        #
        # step12 = [
        #     driver.find_element_by_accessibility_id("ic check big").click()
        #         ]

        n = len(step1)
        print(n)

        i = 0
        while i<4:
            n = len(step1)
            print(n)


        def rnd_step_tour(self):
            n=2
            step_num = random.randint(1, n)
            return step_num



    def lobby_loaded (self):
        contests = self.driver.find_element_by_accessibility_id("Contests")
        league_card = self.driver.find_element_by_xpath("//XCUIElementTypeCell[3]")
        if contests.is_displayed() and league_card.is_displayed():
            return True

    def destroy (self):
        self.driver.quit()



