characteristics = {
    'hair': {
        'black': 'CCAGCAATCGC',
        'brown': 'GCCAGTGCCG',
        'blonde': 'TTAGCTATCGC'
    },
    'face': {
        'square': 'GCCACGG',
        'round': 'ACCACAA',
        'oval': 'AGGCCTCA'
    },
    'eyes': {
        'blue': 'TTGTGGTGGC',
        'green': 'GGGAGGTGGC',
        'brown': 'AAGTAGTGAC'
    },
    'gender': {
        'female': 'TGAAGGACCTTC',
        'male': 'TGCAGGAACTTC'
    },
    'race': {
        'white': 'AAAACCTCA',
        'black': 'CGACTACAG',
        'asian': 'CGCGGGCCG'
    }
}

suspects = {
    'Eva': {
        'hair': 'blonde',
        'face': 'oval',
        'eyes': 'blue',
        'gender': 'female',
        'race': 'white'
    },
    'Larisa': {
        'hair': 'brown',
        'face': 'oval',
        'eyes': 'brown',
        'gender': 'female',
        'race': 'white'
    },
    'Matej': {
        'hair': 'black',
        'face': 'oval',
        'eyes': 'blue',
        'gender': 'male',
        'race': 'white'
    },
    'Miha': {
        'hair': 'brown',
        'face': 'square',
        'eyes': 'green',
        'gender': 'male',
        'race': 'white'
    }
}


def lastnosti_krivca():
    '''funkcija vrne slovar z značilnostmi krivca. Key == del telesa, Value = vrsta znacilnosti'''
    with open('dna.txt', 'r', encoding='utf-8') as dna_file:
        dna_seq = dna_file.read()

    slovar = {}
    for del_telesa, slovar_lastnosti in characteristics.items():
        for lastnost, gen in slovar_lastnosti.items():
            if gen in dna_seq:
                slovar[del_telesa] = lastnost
    return slovar


def kdo_kriv():
    for ime, lastnosti in suspects.items():
        print(lastnosti.values(), lastnosti_krivca().values())
        if set(lastnosti.values()) == set(lastnosti_krivca().values()):
            return ime














