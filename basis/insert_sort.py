def insert_sort(list):
    count = len(list)
    for i in range(1, count):
        key = list[i]
        j = i - 1
        while j >= 0:
            if list[j] > key:
                list[j + 1] = list[j]
                list[j] = key
            j -= 1


list = [6, 5, 8, 9, 7, 2, 3, 4, 5, 6]
insert_sort(list)
print(list)
