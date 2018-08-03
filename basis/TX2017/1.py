#给定一个字符串S 可以删除一些字符。是的剩下的串为一个回文

def strtest(str):
    strlist=list(str)
    strlist2=strlist[::-1]
    num=0

    for i in range(len(strlist)):
        for j in range(len(strlist2)):
            if strlist[i] is strlist2[j]:
                print(i,j)
            else:
                num=num+1
                continue
            break
    return num

s="abcdefggfedcbalkl"
print(strtest(s))
