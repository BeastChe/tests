
class FeedNewsHelper:

    def __init__(self, app):
        self.app = app

    def post_download(self):
        driver = self.app.driver
        driver.find_element_by_id("ru.sports.exampleapp:id/txtTitle")