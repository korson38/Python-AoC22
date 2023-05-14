
# getting the data
with open("D:\PythonProjekty\Szkolenie\Avent of Code\\file.txt", "r") as f:
    lista_kcal = []
    x = 0
# iterating through the data
    for line in f:
        if not line.rstrip() == '':
            x += int(line.rstrip())
        else:
            lista_kcal.append(x)
            x = 0
lista_kcal.append(x)
# printing results
najw = max(lista_kcal)
print(najw)

lista_kcal.sort()
print(sum(lista_kcal[-3:]))
