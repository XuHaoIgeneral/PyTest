class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxs = 0
        lock = 0
        va = 0
        for i in nums:
            if i != 1:
                lock = 0
                va = 0
            if i == 1 and lock == 0:
                lock = 1
                va += 1
            elif i == 1 and lock == 1:
                va += 1
            maxs = max(maxs, va)
        return maxs

test=Solution()
lists=[]
test.findMaxConsecutiveOnes()