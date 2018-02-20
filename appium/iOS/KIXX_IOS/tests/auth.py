import pytest
from iOS import iOSSwipeScroll
from General import config
from iOS.KIXX_IOS.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_mail(self,app):
    app.allow()
    app.login_mail(login="chechetkin@sports.ru", password="Qw641025")
    self.driver.swipe(iOSSwipeScroll.right, 300)
    app.profile()
    app.logout()




#
# def test_vk(self):
#     driver = self.driver
#     vk = driver.find_element_by_accessibility_id("ic vk")
#     vk.click()
#     vk = driver.find_element_by_accessibility_id("Phone or email:")
#     vk1 = next(vk)
#     vk1.click()










