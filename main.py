def perfect_shuffle(deck):
    n = len(deck)

    a = deck[:n // 2]
    b = deck[n // 2:]

    mix = []

    for i in range(n // 2):
        mix.append(a[i])
        mix.append(b[i])

    return mix