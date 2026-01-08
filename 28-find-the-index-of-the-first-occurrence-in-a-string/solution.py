class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.find(needle)
        else:
            return -1


# i mean just return haystack.find(needle) also gives 0 and -1 without if else but that;s too short