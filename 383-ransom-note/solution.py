class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        sr = sorted(ransomNote)
        sm = sorted(magazine)   
        
        for ch in sr:
            if ch in sm:
                sm.pop(sm.index(ch))  
            else:
                return False
        
        return True
