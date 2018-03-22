
class User:

    def __init__(self, name=None, login=None, password=None, type_auth=None):
        self.name = name
        self.login = login
        self.password = password
        self.type_auth = type_auth

    def __repr__(self):
        return "%s:%s:%s:%s" % (self.name, self.login, self.password, self.type_auth)

    def __eq__(self, other):
        return self.name == other.name and self.login == other.login and self.password == other.password and self.type_auth == other.type