class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        root = num ** 0.5
        return root.is_integer()
        