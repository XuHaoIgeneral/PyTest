def parameter(list):
    print(id(list))
    print(list)
    list[0]=1
    return

list=[0,0,0,0,0]
print(id(list))
parameter(list)
print(list)