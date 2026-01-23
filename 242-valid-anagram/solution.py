class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
        ss = sorted(s)
        ts = sorted(t)
        if ss==ts:
            return True
        else:
            return False
         
 # i dunno why the code below cannot pass testcase 51.. how do i use this method to make it work #hmmm       
        #chars = []
        # chrt = []
        # sums = 0
        # sumt =0
        # i = 0
        # j =0
        # while i<len(s):
        #     sums = sums + ord(s[i])
        #     i+=1

        # while j<len(t):
        #     sumt = sumt + ord(t[j])
        #     j+=1
        # for ch in s:
        #     chars.append(ch)
        # for th in t:
        #     chrt.append(th)
        # for c in t:
        #     if c not in chars :
        #         return False
        #     elif sums != sumt:
        #         return False
        #     for a in s:
        #         if a not in chrt:
        #             return False
        #         else:
        #             return True
