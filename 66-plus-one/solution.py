from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        l = len(digits)

        for i in range(l):
            num += digits[i] * 10 ** (l - i - 1)

        num += 1

        return list(map(int, str(num)))
