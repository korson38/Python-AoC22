# preparing data to process, crates and data they have inside
with open("DAY5", "r") as file:
    plik = file.read().split("\n\n")
    crates_lth = len(plik[0].split("\n")[-1][1::4])
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
# cleaning crates of empty spots
    for k in crates:
        for j in k:
            if j != ' ':
                my_list.append(j)
        clean_crates[l] = my_list
        my_list = []
        l += 1
# moving things in the same order as they were arranged in the parent crates
moves = plik[1].split("\n")
for line in moves:
    token = line.split(" ")
    qt, sce, dst = map(int, [token[1], token[3], token[5]])
    sce -= 1
    dst -= 1
    clean_crates[dst].extend(clean_crates[sce][-qt:])
    clean_crates[sce] = clean_crates[sce][:-qt]
# tops of the crates
answer = ''
for crate in clean_crates:
    answer += crate[-1]
print(answer)