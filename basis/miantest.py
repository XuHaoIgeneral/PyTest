import copy

lists=[0,1,2,3,4,5,6]

a=copy.deepcopy(lists)
b=copy.deepcopy(lists)
c=copy.deepcopy(lists)

for i in a:
    a.remove(i)
print(a)

for i in range(len(b)):
    print(i)
    del b[i]
print(b)

for i in range(len(c)):
    c.pop()
print(c)
