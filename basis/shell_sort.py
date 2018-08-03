def shell_sort(lists):
    # 希尔排序
    count = len(lists)
    step = 2
    group = count // step
    while group > 0:  # 通过group增量分组循环
        for i in range(0, group):
            j = i + group
            while j < count:  # 分组中key值的索引，通过增量自增
                k = j - group
                key = lists[j]
                while k >= 0:  # 分组中进行插入排序
                    if lists[k] > key:
                        lists[k + group], lists[k] = lists[k], key
                    k -= group
                    print('k=',k)
                j += group
                print('j=', j)
        group //= step
    return lists


list = [6, 5, 8, 9, 7, 2, 3, 4, 5, 9, 6,10]

r = shell_sort(list)
print(r)
