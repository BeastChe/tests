
class User:

    def __init__(self, name=None, login=None, password=None):
        self.name = name
        self.login = login
        self.password = password

    def __repr__(self):
        return "%s" % (self.name)