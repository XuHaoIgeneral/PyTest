class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        beg1, beg2 = 0, 0
        end1, end2 = len(nums1) - 1, len(nums2) - 1
        lists = []
        if nums1[len(nums1) - 1] > nums2[0] or nums2[len(nums2) - 1] > nums1[0]:
            mid1 = (len(nums1) + 1) // 2
            mid2 = (len(nums2) + 1) // 2
            value1 = nums1[mid1]
            value2 = nums2[mid2]
            if value1 < value2:
                nums1 = nums1[mid1 + 1:]
                nums2 = nums2[:mid2 - 1]
            elif value1 > value2:
                nums1 = nums1[:mid1 - 1]
                nums2 = nums2[mid2 + 1:]
            else:
                return value1


l=[1,2,3]



