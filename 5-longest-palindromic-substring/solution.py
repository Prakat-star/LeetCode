class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start = end = 0

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        for i in range(len(s)):
            l1, r1 = expand(i, i)
            l2, r2 = expand(i, i + 1)

            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end + 1]



# class Solution:
#     def longestPalindrome(self, s: str) -> str:
        # longest_pal = ""

        # n = len(s)

        # for i in range(n):
        #     for j in range(i + 1, n + 1):
        #         current_pal = s[i:j]
        #         if current_pal == current_pal[::-1]:
        #             if len(current_pal) > len(longest_pal):
        #                 longest_pal = current_pal

        # return longest_pal

#This is O(n^3) time complexity