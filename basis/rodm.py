import random

def TT(num):
    a1=random.random()
    a2=random.random()
    b1=a1*num+1
    b2=a2*num+1
    return b1,b2

l=TT(37)
print(l)