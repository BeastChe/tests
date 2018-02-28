


def test_mail(app):
    app.session.login_mail(login="chechetkin@sports.ru", password="Qw641025")



def test_vk(app):
    app.session.vk_login(login="79670738123", password="qwer123vk")


def test_fb(app):
    app.session.fb_login(login="79654398720", password="qwerfb88")


def test_tw(app):
    app.session.tw_login(login="79884018685", password="qwer4321t")




















