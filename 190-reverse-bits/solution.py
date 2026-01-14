class Solution:
    def reverseBits(self, n: int) -> int:
        b = format(n, '032b') 
        r = b[::-1]
        return int(r, 2)

# don;t mind me , i haven;t studied bit manipulation yet this is all i can do