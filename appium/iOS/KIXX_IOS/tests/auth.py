import pytest

from iOS.KIXX_IOS.model.user import User
from iOS.KIXX_IOS.fixture.user_data import UserHelper
from iOS.KIXX_IOS.data import users_data

@pytest.mark.parametrize("user", [users_data.user])
def test_mail(app, user):
    app.session.login_mail(user)
    assert app.lobby_loaded() is True
    assert app.user_data.get_user_name().is_displayed()
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





















