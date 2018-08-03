class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        lists = [[1], [1, 1]]
        if numRows <= 2:
            return lists

        for i in range(2, numRows):
            l = []
            for j in range(i+1):
                if j == 0 or j == i:
                    l.append(1)
                else:
                    re = int(lists[i - 1][j - 1]) + int(lists[i - 1][j])
                    l.append(re)
            lists.append(l)
        return lists

test=Solution()
lists=test.generate(5)
print(lists)