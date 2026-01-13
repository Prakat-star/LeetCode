class Solution:
    def reverse(self, x: int) -> int:
        Int_max = 2**31 - 1
        Int_min = - 2**31
    
        sign = -1 if x<0 else 1
        
        rev = 0 
        x = abs(x)

        while x!=0:
            digit = x%10
            x = x//10

            if rev >Int_max//10 or ( rev == Int_max//10 and digit > 7):
                return 0

            rev = rev*10 + digit
        return rev * sign