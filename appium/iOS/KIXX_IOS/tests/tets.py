import random
from appium import webdriver
from General import config
from iOS.KIXX_IOS.fixture.session import SessionHelper
from iOS.KIXX_IOS.fixture.user_data import UserHelper




def tour_kek(self):
    driver = self.driver
    step1 = [
        driver.find_element_by_accessibility_id("DO IT FOR ME").click(),
        driver.find_element_by_accessibility_id("Tap position F to pick a forward").click()
    ]
    step2 = [
        driver.find_element_by_accessibility_id("GOT IT").click(),
        driver.find_element_by_accessibility_id("AVG means player’s average points in last 10 games").click()
    ]
    step3 = [
        driver.find_element_by_accessibility_id("GOT IT").click(),
        driver.find_element_by_accessibility_id(
            "The players are rated from 1 to 3 stars. Your budget is restricted").click()
    ]
    step4 = [
        driver.find_element_by_accessibility_id("PICK FOR ME").click(),
        driver.find_element_by_accessibility_id("plus").click()
        # --ИМЯ ИГРОКА-- is a really good forward. Pick him now!
    ]
    step5 = [
        driver.find_element_by_accessibility_id("GOT IT").click(),
        driver.find_element_by_accessibility_id("Your team grows! And your budget is declining").click()
    ]
    step6 = [
        driver.find_element_by_accessibility_id("DO IT FOR ME").click(),
        driver.find_element_by_accessibility_id("Midfielder").click(),
        driver.find_element_by_accessibility_id("Tap to see other positions").click()
    ]
    step7 = [
        driver.find_element_by_accessibility_id("PICK FOR ME").click(),
        driver.find_element_by_accessibility_id("plus").click()
    ]
    step8 = [
        driver.find_element_by_accessibility_id("DO IT FOR ME").click(),
        driver.find_element_by_accessibility_id("Back").click(),
        driver.find_element_by_accessibility_id("Tap to see your team and vacant positions").click()
    ]
    step9 = [
        driver.find_element_by_xpath("//XCUIElementTypeOther[2]/XCUIElementTypeButton").click()
    ]
    step10 = [
        driver.find_element_by_accessibility_id("DO IT FOR ME").click()
        # "You have --кол-во звёзд-- stars for --кол-во игроков-- players.Use Cost filter to see cheaper ones"
    ]
    step11 = [
        driver.find_element_by_accessibility_id("PICK FOR ME").click()
    ]
    step12 = [
        driver.find_element_by_accessibility_id("ic check big").click()
    ]
    n = len(step1)
    print(n)
    i = 0
    while i < 12:
        n = len(step1)
        print(n)

    def rnd_step_tour(self):
        n = 2
        step_num = random.randint(1, n)
        return step_num









