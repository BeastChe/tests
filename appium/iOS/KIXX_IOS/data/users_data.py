from iOS.KIXX_IOS.model.user import User
import random

user = [
    User(name="Mr Boss", login="xer@mailinator.com", password="password", type_auth="email"),
    User(name="Big Papa", login="bigpapa@mailinator.com", password="password", type_auth="email"),
    User(name="Дмитрий Огуречный", login="ogurchik@mailinator.com", password="password1", type_auth="email"),

    User(name="Корнюшон Аманжолов", login="79654399637", password="vk123qwe", type_auth="vk"),

    User(name="Cornishon Mamanjopa", login="79654399637", password="fb123qwe", type_auth="fb"),

    User(name="Cornishon Twitjopa", login="79654399637", password="tw123qwe", type_auth="tw")
    ]


def sorted_user():
    selected_type_auth = "email"
    sort_user = []
    i = 0
    while i < len(user):
        if user[i].type_auth == selected_type_auth:
            sort_user.append(user[i])
        i += 1
    i = random.randint(0, len(sort_user) - 1)
    received_user = sort_user[i]
    return received_user


print(sorted_user())


