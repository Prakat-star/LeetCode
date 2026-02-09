from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        com = set()
        for i in nums2:
            if i in nums1:
                com.add(i)
        return list(com)
        