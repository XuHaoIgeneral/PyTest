def quick_sort(list, left, right):
    if left >= right:
        return
    low = left
    hight = right
    key = list[low]
    while right > left:
        while right > left and list[right] > key:
            right = right - 1
        list[left] = list[right]
        while right > left and list[left] <= key:
            left = left + 1
        list[right] = list[left]
    list[right] = key
    quick_sort(list, low, left - 1)
    quick_sort(list, left + 1, hight)

list = [6, 5, 8, 9, 7, 2, 3, 4, 5, 6]
quick_sort(list, 0, len(list) - 1)
print(list)

def quicksort(list):
    if len(list)<2:
        return list
    else:
        midpivot = list[0]
        lessbeforemidpivot = [i for i in list[1:] if i<=midpivot]
        biggerafterpivot = [i for i in list[1:] if i > midpivot]
        finallylist = quicksort(lessbeforemidpivot)+[midpivot]+quicksort(biggerafterpivot)
        return finallylist


list = [6, 5, 8, 9, 7, 2, 3, 4, 5, 6]
l=quicksort(list)
print(list)
print(l)
