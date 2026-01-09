from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left,right = 0 , len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if target == nums[mid]:
                return mid
            elif nums[mid]<target:
                left= mid+1
            else:
                right=mid-1
            
        return left
# [1,3,4,5,6,7,8,9,10,11]
# len = 10
# mid = 4
# num[mid]=6
# target = 2
# nums[mid]>target
# right = mid-1 = 4-1 = 3
# mid = 1
# num[mid]=3
# right = mid-1 = 0
# mid=0
# nums[mid]<target
# left = left+1 = 1
# return left 
# 1



        