from string import ascii_letters

# getting the data from file
with open("<your path>", "r") as f:
    plecaki = [i.strip() for i in f.readlines()]
    cs = []
    w = []
    element = None
    suma = 0
# preparing data to analyze
    for x in plecaki:
        cs.append(x[:len(x) // 2])
        cs.append(x[len(x) // 2:])
# analyzing the data
    for y in cs[::2]:
        for el in y:
            x = cs.index(y) + 1
            if el in cs[x]:
                element = el
        w.append(element)
# counting the sum of priorities
    for pr in w:
        for num, char in enumerate(ascii_letters):
            if pr == char:
                suma += num + 1
    print(suma)
# part two, iterating through the data
    suma2 = 0
    badge = []
# checking which elements perform 3 times
    for x in plecaki[::3]:
        for el in x:
            ind = plecaki.index(x) + 1
            ind_1 = plecaki.index(x) + 2
            if el in plecaki[ind] and el in plecaki[ind_1]:
                element = el
        badge.append(element)
# counting the sum of the badges priority
    for badg in badge:
        for num, char in enumerate(ascii_letters):
            if badg == char:
                suma2 += num + 1
    print(suma2)

