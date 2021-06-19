import json

with open('users.json', 'r', encoding='utf-8') as users_file:
    users_list = json.loads(users_file.read())

def izpis():
    with open('users.json', 'r', encoding='utf-8') as users_file:
        users_list = json.loads(users_file.read())
    for person in users_list:
        ime, priimek = person['name'].split()
        lat = person['address']['geo']['lat']
        cp = person['company']['catchPhrase']
        print(ime)
        print(priimek)
        print(lat)
        print(cp)
        print('-' * 50)


priimek = input('Vpiši priimek: ')
for person in users_list:
    if priimek.lower() in person['name'].lower():
        ime, priimek = person['name'].split()
        lat = person['address']['geo']['lat']
        cp = person['company']['catchPhrase']
        print(ime)
        print(priimek)
        print(lat)
        print(cp)
        print('-' * 50)

