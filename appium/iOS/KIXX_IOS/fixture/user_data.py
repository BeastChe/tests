from iOS.KIXX_IOS.model.user import User


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
        name = driver.find_element_by_accessibility_id("Mr Boss")
        return name







