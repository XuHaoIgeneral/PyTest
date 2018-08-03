def bubble_sory(list):
    count = len(list)
    for i in range(count):
        ...
        for j in range(0, count - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]


list = [6, 5, 8, 9, 7, 2, 3, 4, 5, 6]
bubble_sory(list)
print(list)
