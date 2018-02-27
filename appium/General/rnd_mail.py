import random


#MAIL
domains = ["bla.com", "kuku.ru", "kek.kek", "kek.lol", "ped.com", "byba.ru", "koko.rnd", "pis.xx"]
letters = [chr(y) for y in range(ord('a'),ord('z')+1)]

def random_domain(domains):
        return domains[random.randint(0, len(domains) - 1)]

def random_name():
    name = ""
    for i in range(10):
        name = name + letters[random.randint(0, 25)]
    return name

def generate_random_emails():
         email = str(random_name()) + "@" + str(random_domain(domains))
         return email