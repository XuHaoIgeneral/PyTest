# def print_num(n):
#     for i in range(1, n + 1):  # 注意很多编程语言使用的都是 从 0 开始的左闭右开区间, python 也不例外
#         print(i)
#
#
# def listArray(lists):
#     my_container = ['lily', 'lucy', 'tom']
#     index = 0
#     for element in my_container:
#         print('{} {}'.format(index, element))
#         index += 1
#
#     # good
#     for index, element in enumerate(my_container):
#         print('%d %s' % (index, element))
#
# def tupleL(x,args):
#     print(args)
#     if len(args)==0:
#         return x
#     n=x
#     if len(args)>0:
#         j=args.pop(0)
#         x1=n+j
#         return tupleL(x1,args)
#
# if __name__ == '__main__':
#     a=tupleL(2,[1,2,3,4,5])
#     print(a)
#

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or s=="":
            return 0
        lists = list(s)
        rtype = 1
        conlist = []
        conlist.append(lists[0])
        container = len(conlist)
        for i in range(1, len(lists)):
            con = lists[i]
            if con not in conlist:
                conlist.append(con)
                container = len(conlist)
            else:
                for k in range(len(conlist)):
                    if con==conlist[k]:
                        if rtype<len(conlist):
                            rtype=len(conlist)
                        conlist=conlist[k+1:]
                        conlist.append(con)
                        container=len(conlist)
                        break
                if container > rtype:
                    rtype = container
        if container > rtype:
            rtype = len(conlist)
        return rtype

a=Solution()
b=a.lengthOfLongestSubstring("add")
print(b)