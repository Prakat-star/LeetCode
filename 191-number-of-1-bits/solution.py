class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        b = bin(n) 
        bi = str(b[2:])
        for i in range(len(bi)):
            if bi[i]=='1':
                count +=1
        return count