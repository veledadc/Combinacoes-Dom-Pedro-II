from itertools import permutations

nome = ['Pedro', 'de Alcântara', 'João', 'Carlos', 'Leopoldo', 
        'Salvador', 'Bibiano', 'Francisco', 'Xavier', 'de Paula', 
        'Leocádio', 'Miguel', 'Gabriel', 'Rafael', 'Gonzaga', 
        'de Bragança', 'Bourbon']
for subset in permutations(nome, 3):
    print(subset)