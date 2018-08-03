def test(num,l=[]):
    print(id(l))
    if num==0:
        l2=[]
        for i in range(len(l)):
            l2.append(l.pop())
        l2_len=len(l2)
        n=0
        for k in l2:
            l2_len = l2_len - 1
            n=n+k*(10**l2_len)
        num=n
        return num
    n1=num%2
    n2=num//2
    l.append(n1)
    return test(n2)

num=input("input your num")
num=int(num)
l=test(num)
print(test(num))






