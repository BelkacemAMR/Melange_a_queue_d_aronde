def perfect_shuffle(deck):
    n = len(deck)

    a = deck[:n // 2]
    b = deck[n // 2:]

    mix = []

    for i in range(n // 2):
        mix.append(a[i])
        mix.append(b[i])

    return mix

# TEST :

# Créer une liste de cartes ou de nombres

deck = [1, 2, 3, 4, 5, 6, 7, 8]

# Appeler la fonction perfect_shuffle()

shuffled_deck = perfect_shuffle(deck)

# Vérifier si le résultat est correct

print(shuffled_deck)

# Résultat : [1, 5, 2, 6, 3, 7, 4, 8]