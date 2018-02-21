import pytest

from iOS.KIXX_IOS.fixsture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_mail(app):
    app.allow()
    app.session.login_mail(login="chechetkin@sports.ru", password="Qw641025")
    app.menu()
    app.profile()
    app.session.logout()




#
# def test_vk(self):
#     driver = self.driver
#     vk = driver.find_element_by_accessibility_id("ic vk")
#     vk.click()
#     vk = driver.find_element_by_accessibility_id("Phone or email:")
#     vk1 = next(vk)
#     vk1.click()










