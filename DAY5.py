with open("DAY5", "r")as file:
    plik = file.read().split("\n\n")
    crates_lth = len(plik[0].split("\n")[-1][1::4])
    crates_hgt = len(plik[0].split("\n"))-1
    crates = [[] for _ in range(crates_lth)]
    clean_crates = [[] for _ in range(crates_lth)]
    text = plik[0][1::4]
    j = 0
    for x in crates:
        for y in text[j::9]:
            x.append(y)
        j += 1
    for x in crates:
        x.pop(-1)
    my_list = []
    crates = [crate[::-1] for crate in crates]
    l = 0
    for k in crates:
        for j in k:
            if j != ' ':
                my_list.append(j)
        clean_crates[l] = my_list
        my_list = []
        l += 1
moves = plik[1].split("\n")
for line in moves:
    token = line.split(" ")
    qt, sce, dst = map(int, [token[1], token[3], token[5]])
    sce -= 1
    dst -= 1

    for _ in range(qt):
        rmv = clean_crates[sce].pop()
        clean_crates[dst].append(rmv)
answer = ''
for crate in clean_crates:
    answer += crate[-1]
print(answer)