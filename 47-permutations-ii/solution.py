from typing import List
from collections import Counter

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        count = Counter(nums)
        def backtrack(path):
            if len(path) == len(nums):
                result.append(path[:])
                return      
            for num in count:
                if count[num] > 0:
                    path.append(num)
                    count[num] -= 1
                    backtrack(path)
                    path.pop()
                    count[num] += 1
        backtrack([])
        return result