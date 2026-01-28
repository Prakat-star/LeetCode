from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen  = set()
        for n in nums:
            seen.add(n)
        return sum(seen) - (sum(nums)-sum(seen))


        # tl = sum(nums)
        # ts = sum(seen)
        # tt = tl-ts
        # return ts-tt



        