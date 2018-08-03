def odd(n):
    for i in range(0, n + 1, 2):
        print("执行前",i)
        msg = yield i
        print('msg=',msg)
        print("执行后", i)
    return "哈哈哈"

gen = odd(5)

print( next(gen) )#0
print( next(gen) )#2
print( gen.send("传入数据") )

try:
     print( next(gen) )
except StopIteration as e :
    print(e.value)      #会打印出 哈哈哈， 也就是odd函数的返回值