from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            res += [curr + [num] for curr in res]
        return res

# le me explain this to you nowww
# seee we create res = [[]] well everyone knows what this means right
# jus in case le me tell you it creates an empty subset
# now for each num in nums we loop through each num
# res = res + [curr + [num] for curr in res]
# for example lets say we have nums = [1,2,3]
# so first num is 1
# what this does is return
# res = [[],[1]] first res had [] now it have 1 as well so res becomes [[],[1]] and now it gets interesting
# when num is [2]
# first curr + num curr is [] + [2] = [2] and [1] + [2] is [1,2]
# res becomes [[],[1],[2],[1,2]]
# and when it is [3]
# first curr + num curr is [] + [3] = [3] and [1] + [3] is [1,3] and [2] + [3] is [2,3] and
# [1,2]+[3] is [1,2,3]
# res becomes [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# this works by looping the entire subset for each number...