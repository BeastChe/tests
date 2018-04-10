from iOS.KIXX_IOS.model.user import User
from iOS.KIXX_IOS.data.users_data import user
from iOS.KIXX_IOS.data import users_data
import random


class UserHelper:

    def __init__ (self,app):
        self.app = app


    def user_page(self):
        driver = self.app.driver
        driver.find_element_by_name("icon menu").click()
        driver.find_element_by_xpath("//XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable/XCUIElementTypeCell[1]").click()


    def get_user_name(self, name):
        driver = self.app.driver
        print(name)
        self.user_page()
        search_name = driver.find_element_by_accessibility_id(name)
        #print(search_name)
        return search_name


    def selected_user(self, selected_type_auth):
        sort_user = []
        i = 0
        while i < len(users_data.user):
            if users_data.user[i].type_auth == selected_type_auth:
                sort_user.append(users_data.user[i])
            i += 1
        i = random.randint(0, len(sort_user) - 1)
        received_user = sort_user[i]
        return received_user








