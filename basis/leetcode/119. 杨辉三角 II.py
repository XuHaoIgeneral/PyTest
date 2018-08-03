class Solution:
    def getRow(self, rowIndex, rowlists=[], rows=1):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex < 0:
            return rowlists
        lists = []
        for i in range(rows):
            if i == 0 or i == rows-1:
                lists.append(1)
            else:
                lists.append(rowlists[i-1]+rowlists[i])
        rowIndex -= 1
        rows += 1
        return self.getRow(rowIndex, lists,rows)

test = Solution()
a = test.getRow(3)
print(a)
