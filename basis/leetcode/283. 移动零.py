class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        print(nums)
        count = len(nums)
        if count == 0:
            print(nums)
        if 0 not in nums:
            print(nums)
        zero_nums = 0

        for i in range(count):
            if nums[i] == 0:
                zero_nums += 1
        for j in range(zero_nums):
            nums.remove(0)

        nums.extend([0]*zero_nums)
        print(nums)

test=Solution()
lists=[0,1,0,3,12]
test.moveZeroes(lists)