
from General import rnd_mail

def test_signup(app):
    app.session.signup_mail (name = rnd_mail.random_name(), email = rnd_mail.generate_random_emails(),  password="password")
    app.menu()
    app.profile()
    app.session.logout()