def testFun():
    temp=[lambda x:i*x for i in range(4)]
    print(id(temp))
    print("a")
    return temp

for everyLambda in testFun():
    print(everyLambda(2))