class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i

a=Solution()
lists=[0,1,2,2,3,0,4,2]
b=a.removeElement(lists,2)
print(b)
print(lists)
