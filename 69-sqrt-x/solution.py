class Solution:
    def mySqrt(self, x: int) -> int:
        precision= 0.000001
        n = x
        if x == 1 or x == 0:
            return x
        else:
            while True:
                root = (n + x / n) / 2
                if abs(root - n) < precision:
                    return int(root)
                n = root
