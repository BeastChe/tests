from iOS.KIXX_IOS.model.user import User
from iOS.KIXX_IOS.data import users_data


class UserHelper:

    def __init__ (self,app):
        self.app = app

    def user_page(self):
        driver = self.app.driver
        driver.find_element_by_name("icon menu").click()
        driver.find_element_by_xpath("//XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable/XCUIElementTypeCell[1]").click()


    def get_user_name(self):
        driver = self.app.driver
        self.user_page()
        # БАГ
        name = driver.find_element_by_accessibility_id(users_data.email[0].name)
        print(users_data.email[0].name)
        #name = driver.find_element_by_accessibility_id("Mr Boss")
        return name







