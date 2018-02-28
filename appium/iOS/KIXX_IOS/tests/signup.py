
from General import rnd_mail


def test_signup(app):
    app.get_started()
    app.session.signup_mail (name = rnd_mail.random_name(), email = rnd_mail.generate_random_emails(),  password="password")
    app.session.logout_from_lobby()

def test_vk(app):
    app.get_started()
    app.session.vk_login(login="79670738123", password="qwer123vk")
    app.session.logout_from_lobby()


def test_fb(app):
    app.get_started()
    app.session.fb_login(login="79654398720", password="qwerfb88")
    app.session.logout_from_lobby()


def test_tw(app):
    app.get_started()
    app.session.tw_login(login="79884018685", password="qwer4321t")
    app.session.logout_from_lobby()

