from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = nums1 + nums2
        num.sort()
        l = len(num)
        if l%2 != 0:
            return num[l//2]
        return (num[l//2] + num[l//2 - 1])/2
        
  
        # Apparently this is how we get mean even tho this code does satisfies all cases , it is not the way
        # s1 = sum(nums1)
        # s2 = sum(nums2)
        # s= s1+s2
        # l1 = len(nums1)
        # l2 = len(nums2)
        # l = l1 + l2
        # return float(s/l) 