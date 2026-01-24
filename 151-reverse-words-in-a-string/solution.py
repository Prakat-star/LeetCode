class Solution:
    def reverseWords(self, s: str) -> str:
        sl=s.split()
        sl.reverse()
        return " ".join(sl)
        