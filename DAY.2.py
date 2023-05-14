
# part 1
with open("<your path>", "r") as f:
    rounds = [i.replace(" ", "") for i in f.read().strip().split("\n")]
    wynik = 0
    for round in rounds:
        if round == 'AX' or round == 'BY' or round == 'CZ':wynik += 3
        elif round == 'AY' or round == 'BZ' or round == 'CX': wynik += 6
        if round[1] == 'X': wynik += 1
        elif round[1] == 'Y': wynik += 2
        elif round[1] == 'Z': wynik += 3
    print(wynik)
# part 2
with open(("<your path>", "r") as f:
    rounds = [i.replace(" ", "") for i in f.read().strip().split("\n")]
    wynik = 0
    for round in rounds:
        if round == 'AZ' or round == 'BZ' or round == 'CZ':wynik += 6
        elif round == 'AY' or round == 'BY' or round == 'CY': wynik += 3
        if round == 'AX' or round == 'BZ' or round == 'CY': wynik += 3
        elif round == 'AY' or round == 'BX' or round == 'CZ': wynik += 1
        elif round == 'AZ' or round == 'BY' or round == 'CX': wynik += 2
    print(wynik)
