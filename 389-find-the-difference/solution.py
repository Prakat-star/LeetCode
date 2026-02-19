class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ass = 0
        att = 0
        for i in s:
            ass = ass + ord(i)
        for j in t:
            att = att + ord(j)
        return chr(att - ass)