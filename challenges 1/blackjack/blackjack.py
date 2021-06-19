import random

class Blackjack:
    def __init__(self):
        self.kupcek = {'srce': [2,3,4,5,6,7,8,9,10,10,10,10],
                       'karo': [2,3,4,5,6,7,8,9,10,10,10,10],
                       'pik': [2,3,4,5,6,7,8,9,10,10,10,10],
                       'kriz': [2,3,4,5,6,7,8,9,10,10,10,10]}

        self.igralceve_karte = []
        self.racunalnikove_karte = []

    def igralec_potegne_karto(self):
        while True:
            barva = random.choice(list(self.kupcek.keys()))
            if self.kupcek[barva]:
                vrednost_karte = random.choice(self.kupcek[barva])
                break
        self.igralceve_karte.append(vrednost_karte)

    def racunalnik_potegne_karto(self):
        while True:
            barva = random.choice(list(self.kupcek.keys()))
            if self.kupcek[barva]:
                vrednost_karte = random.choice(self.kupcek[barva])
                break
        self.racunalnikove_karte.append(vrednost_karte)

    def igralcev_sestevek(self):
        return sum(self.igralceve_karte)

    def racunalnikov_sestevek(self):
        return sum(self.racunalnikove_karte)



igra = Blackjack()
igralec = input('Vpiši svoje ime in pritisni ENTER: ')
input('Za začetek pritisni ENTER: ')

igra.igralec_potegne_karto()
igra.racunalnik_potegne_karto()
igra.racunalnik_potegne_karto()

while True:
    print(f'{igralec} tvoje karte so: {igra.igralceve_karte} ')
    print(f'Računalnikove karte so : {igra.racunalnikove_karte}')
    odgovor_igralec = input(f'{igralec } če želiš še eno karto vpiši Y, če želiš končati, pritisni enter: ')
    if odgovor_igralec.lower() == 'y':
        igra.igralec_potegne_karto()
    else:
        break
    print('-' * 50)

print(f'{igralec} tvoje karte so: {igra.igralceve_karte} ')
print(f'Računalnikove karte so : {igra.racunalnikove_karte}')

if igra.igralcev_sestevek() > 21:
    print(f'{igralec}, na žalost je tvoj seštevek kart višji od 21, kar pomeni, da si izgubil stavo.')

elif igra.igralcev_sestevek() > igra.racunalnikov_sestevek():
    print(f'Čestitke, zmagal si.')

elif igra.igralcev_sestevek() < igra.racunalnikov_sestevek():
    print(f'Seštevek tvojih kart je manjše od računalnikovih.')

else:
    print('Rezultata sta izenačena. Nihče ni zmagal')














