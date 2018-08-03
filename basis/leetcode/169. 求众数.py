"""
给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在众数。
示例 1:
输入: [3,2,3]
输出: 3
示例 2:
输入: [2,2,1,1,1,2,2]
输出: 2
"""
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = len(nums)
        if count == 0:
            raise ("this is a illegal list")
        mode = count // 2
        num_set = set(nums)
        num_dict = {}
        for i in num_set:
            num_dict[i] = 0

        for i in nums:
            num_dict[i]=num_dict[i]+1

        maxs=0
        maxs_nums=None
        for key,value in num_dict.items():
            if value>maxs and value>mode:
                maxs=value
                maxs_nums=key
        return maxs_nums

test=Solution()
lists=[3,2,3]
test.majorityElement(lists)