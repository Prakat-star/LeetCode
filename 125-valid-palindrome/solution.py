class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ' '.join(c.lower() for c in s if c.isalnum())
        rst = st[::-1]
        if st==rst:
            return True
        else:
            return False        