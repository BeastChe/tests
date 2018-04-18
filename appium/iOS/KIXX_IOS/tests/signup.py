from iOS.KIXX_IOS.model.user import User
from General import rnd_mail


def test_signup(app):
    driver = app.driver
    user = User(name=rnd_mail.random_name(), login=rnd_mail.generate_random_emails(),  password="password")
    app.get_started()
    app.session.signup_mail(user)
    assert app.lobby_loaded() is True
    app.user_data.user_page()
    assert driver.find_element_by_accessibility_id(user.name).is_displayed()
    app.session.logout()

def test_vk(app):
    app.get_started()
    driver = app.driver
    user = app.user_data.selected_user(selected_type_auth="vk")
    app.session.vk_login(user)
    assert app.lobby_loaded() is True
    app.user_data.user_page()
    assert driver.find_element_by_accessibility_id(user.name).is_displayed()
    app.session.logout()


def test_fb(app):
    app.get_started()
    driver = app.driver
    user = app.user_data.selected_user(selected_type_auth="fb")
    app.session.fb_login(user)
    assert app.lobby_loaded() is True
    app.user_data.user_page()
    assert driver.find_element_by_accessibility_id(user.name).is_displayed()
    app.session.logout()


def test_tw(app):
    app.get_started()
    driver = app.driver
    user = app.user_data.selected_user(selected_type_auth="tw")
    app.session.tw_login(user)
    assert app.lobby_loaded() is True
    app.user_data.user_page()
    assert driver.find_element_by_accessibility_id(user.name).is_displayed()
    app.session.logout()










