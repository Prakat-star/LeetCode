class Solution:
    def addDigits(self, num: int) -> int:
        while num>=10:
            sum = 0
            for d in str(num):
                sum = sum + int(d)
            num = sum
        return num