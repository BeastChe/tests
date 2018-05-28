
from appium import webdriver
from General import new_config
from Android.etalon.fixsture.session import SessionHelper
from Android.etalon.fixsture.feed_news import FeedNewsHelper


class Application:

    def __init__(self):
        desired_caps = new_config.new_desired_caps()
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)
        self.session = SessionHelper(self)
        self.feed_news = FeedNewsHelper(self)

    def is_valid(self):
        try:
            if 1 == 1:
                return True
        except:
            return False

    def destroy(self):
        self.driver.quit()