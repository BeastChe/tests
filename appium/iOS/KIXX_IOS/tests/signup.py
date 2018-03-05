from iOS.KIXX_IOS.model.user import User
from General import rnd_mail


def test_signup(app):
    app.get_started()
    app.session.signup_mail(User(name=rnd_mail.random_name(), login=rnd_mail.generate_random_emails(),  password="password"))

def test_vk(app):
    app.get_started()
    app.session.vk_login(User(login="79670738123", password="qwer123vk"))


def test_fb(app):
    app.get_started()
    app.session.fb_login(User(login="79654398720", password="qwerfb88"))


def test_tw(app):
    app.get_started()
    app.session.tw_login(User(login="79884018685", password="qwer4321t"))

