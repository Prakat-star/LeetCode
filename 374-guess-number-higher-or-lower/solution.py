# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
def guess(num: int) -> int:
    picked = 2
    if num > picked:
        return -1
    elif num < picked:
        return 1
    else:
        return 0
class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        while low <= high:
            mid = (low + high) // 2
            res = guess(mid)   
            if res == 0:
                return mid
            elif res == -1:
                high = mid - 1
            else:
                low = mid + 1
        