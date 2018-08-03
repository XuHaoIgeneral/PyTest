"""
给定一个字符串 s，你可以通过在字符串前面添加字符将其转换为回文串。找到并返回可以用这种方式转换的最短回文串。
示例 1:
输入: "aacecaaa"
输出: "aaacecaaa"
示例 2:
输入: "abcd"
输出: "dcbabcd"
"""

class Solution:
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list=list(s)
        palindrome_list=[]
        p_list=s_list
        for i in range(len(s_list)-1,-1,-1):
            palindrome_list.append(s_list[i])

        for i in range(len(p_list)):

            for j in range(len(s_list)-1-i,-1,-1):


                if p_list[i]==s_list[j]:
                    lock=True
                    o1=j-1
                    o2=i+1
                    while lock==True and o:



test=Solution()
str="abcda"
test.shortestPalindrome(str)
