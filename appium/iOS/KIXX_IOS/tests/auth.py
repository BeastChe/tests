import pytest

from iOS.KIXX_IOS.model.user import User
from iOS.KIXX_IOS.fixture import user_data
from iOS.KIXX_IOS.data import users_data


def test_mail(app):
    driver = app.driver
    user = app.user_data.selected_user(selected_type_auth = "email")
    #user = app.user_data.selected_user(user_data.auth_type.email)
    app.session.login_mail(user)
    assert app.lobby_loaded() is True
    app.user_data.user_page()
    assert driver.find_element_by_accessibility_id(user.name).is_displayed()
    app.session.logout()

def test_vk(app):
    app.session.vk_login(User(login="79670738123", password="qwer123vk"))


def test_fb(app):
    app.session.fb_login(User(login="79654398720", password="qwerfb88"))


def test_tw(app):
    app.session.tw_login(User(login="79884018685", password="qwer4321t"))



def test_logout(app):
    app.session.login_mail(User(login="chechetkin@sports.ru", password="Qw641025"))
    app.session.logout_from_lobby()





















