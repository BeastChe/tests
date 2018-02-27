import pytest

from iOS.KIXX_IOS.fixsture.application import Application




def test_mail(app):
    app.allow()
    app.login()
    app.session.login_mail(login="chechetkin@sports.ru", password="Qw641025")
    app.menu()
    app.profile()
    app.session.logout()


def test_vk(app):
    app.session.vk_login(login="79670738123", password="qwer123vk")
    app.menu()
    app.profile()
    app.session.logout()


def test_fb(app):
    app.session.fb_login(login="79654398720", password="qwerfb88")
    app.menu()
    app.profile()
    app.session.logout()


def test_tw(app):
    app.session.tw_login(login="79884018685", password="qwer4321t")
    app.menu()
    app.profile()
    app.session.logout()


#    ("GET STARTED")

















