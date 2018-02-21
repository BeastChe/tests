
class SessionHelper:

    def __init__ (self,app):
        self.app = app


    def login_mail(self, login, password):
        driver = self.app.driver
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


    def logout(self):
        driver = self.app.driver
        logout = driver.find_element_by_accessibility_id("ic logout")
        logout.click()
        yes = driver.find_element_by_accessibility_id("YES")
        yes.click()