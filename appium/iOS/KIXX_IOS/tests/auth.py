


def test_mail(app):
    driver = app.driver
    user = app.user_data.selected_user(selected_type_auth="email")
    app.session.login_mail(user)
    assert app.lobby_loaded() is True
    app.user_data.user_page()
    assert driver.find_element_by_accessibility_id(user.name).is_displayed()
    app.session.logout()

def test_vk(app):
    driver = app.driver
    user = app.user_data.selected_user(selected_type_auth="vk")
    app.session.vk_login(user)
    assert app.lobby_loaded() is True
    app.user_data.user_page()
    assert driver.find_element_by_accessibility_id(user.name).is_displayed()
    app.session.logout()


def test_fb(app):
    driver = app.driver
    user = app.user_data.selected_user(selected_type_auth="fb")
    app.session.fb_login(user)
    assert app.lobby_loaded() is True
    app.user_data.user_page()
    assert driver.find_element_by_accessibility_id(user.name).is_displayed()
    app.session.logout()


def test_tw(app):
    driver = app.driver
    user = app.user_data.selected_user(selected_type_auth="tw")
    app.session.tw_login(user)
    assert app.lobby_loaded() is True
    app.user_data.user_page()
    assert driver.find_element_by_accessibility_id(user.name).is_displayed()
    app.session.logout()