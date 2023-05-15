# preparing data
with open(<your path>)as f:
    counter = 0
# iterating through the lines
    for line in f:
        list = []
        x = line.strip()
        digit = ''
        for char in x:
            if char.isdigit():
                digit = digit + char
            else:
                list.append(digit)
                digit = ''
        list.append(digit)
# checking if l_list contains elements from r_list and conversely
        left_list = [x for x in range(int(list[0]),int(list[1])+1)]
        right_list = [x for x in range(int(list[2]),int(list[3])+1)]
        if all(elem in left_list for elem in right_list) or all(elem in right_list for elem in left_list):
            counter += 1
    print(counter)

# If u want to check which elements overlaps on each other use this code instead that in line 19
# if any(elem in left_list for elem in right_list) or any(elem in right_list for elem in left_list):
