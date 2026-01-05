class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]
        if s == x:
            print("palindrome")
        else :
            print("not palindrome") 