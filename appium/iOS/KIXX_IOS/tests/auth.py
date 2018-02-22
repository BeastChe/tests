import pytest

from iOS.KIXX_IOS.fixsture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

#
# def test_mail(app):
#     app.allow()
#     app.session.login_mail(login="chechetkin@sports.ru", password="Qw641025")
#     app.menu()
#     app.profile()
#     app.session.logout()





def test_vk(app):
    app.vk_login()


    # vk = driver.driver.find_element_by_xpath("//XCUIElementTypeOther[1]")
    # vk.send_keys(login)
    # k = driver.driver.find_element_by_xpath("//XCUIElementTypeOther[1]")
    # vk.send_keys(password)














