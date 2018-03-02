from iOS.KIXX_IOS.model.user import User

def test_mail(app):
    app.session.login_mail(User(login="xer@mailinator.com", password="password"))
    # app.menu()
    # app.click_profile()
    #assert app.user.get_user_name == "Mr Boss"


def test_vk(app):
    app.session.vk_login(User(login="79670738123", password="qwer123vk"))


def test_fb(app):
    app.session.fb_login(User(login="79654398720", password="qwerfb88"))



def test_tw(app):
    app.session.tw_login(User(login="79884018685", password="qwer4321t"))



def test_logout(app):
    app.session.login_mail(User(login="chechetkin@sports.ru", password="Qw641025"))
    app.session.logout_from_lobby()





















