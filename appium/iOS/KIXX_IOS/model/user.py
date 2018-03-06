
class User:

    def __init__(self, name=None, login=None, password=None):
        self.name = name
        self.login = login
        self.password = password

    def __repr__(self):
        return "%s:%s:%s" % (self.name, self.login, self.password)

    def __eq__(self, other):
        return self.name == other.name and self.login == other.login and self.password == other.password