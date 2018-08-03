"""
在一个由小写字母构成的字符串 S 中，包含由一些连续的相同字符所构成的分组。
例如，在字符串 S = "abbxxxxzyy" 中，就含有 "a", "bb", "xxxx", "z" 和 "yy" 这样的一些分组。
我们称所有包含大于或等于三个连续字符的分组为较大分组。找到每一个较大分组的起始和终止位置。
最终结果按照字典顺序输出。
示例 1:

输入: "abbxxxxzzy"
输出: [[3,6]]
解释: "xxxx" 是一个起始于 3 且终止于 6 的较大分组。
示例 2:

输入: "abc"
输出: []
解释: "a","b" 和 "c" 均不是符合要求的较大分组。
示例 3:

输入: "abcdddeeeeaabbbcd"
输出: [[3,5],[6,9],[12,14]]
说明:  1 <= S.length <= 1000
"""

class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        lists=list(S)
        threshold=3
        lock=0
        re=[]
        re_son=[0,0]
        word=None
        word_nums=0
        for i in range(len(lists)):
            if word is None or lock==0:
                word=lists[i]
                lock=1
                word_nums+=1
                re_son[0]=i
            if lock==1:
                if lists[i]==word:
                    word_nums+=1
                    re_son[1] = i
                    re.append(re_son)
                else:
                    re_son[0] = i
                    word_nums=0
                    re_son = [0, 0]
        print(re)


test=Solution()
str="abcdddeeeeaabbbcd"
test.largeGroupPositions(str)