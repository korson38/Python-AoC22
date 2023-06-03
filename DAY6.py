# looking for distinct characters in the string
with open("DAY6", "r") as file:
    text = file.read()
    counter = 0
# to solve part 1 type 4 instead of 14
    for x in range(14, len(text)):
        code = set(text[(x-14):x])
        counter += 1
        if len(code) == 14:
# to solve part 1 type 3 instead of 13
            print("we made it " + str(counter+13))
            break
