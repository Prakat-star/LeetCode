from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_left():
            l, r = 0, len(nums) - 1
            idx = -1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1
                if nums[mid] == target:
                    idx = mid
            return idx

        def find_right():
            l, r = 0, len(nums) - 1
            idx = -1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] <= target:
                    l = mid + 1
                else:
                    r = mid - 1
                if nums[mid] == target:
                    idx = mid
            return idx

        first = find_left()
        last = find_right()
        return [first, last]
