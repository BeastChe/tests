

class UserHelper:

    def __init__ (self,app):
        self.app = app

    def get_user_name(self):
        driver = self.app.driver
        name = driver.find_element_by_class_name ("XCUIElementTypeNavigationBar").get_text()
        print(name)
        return name





