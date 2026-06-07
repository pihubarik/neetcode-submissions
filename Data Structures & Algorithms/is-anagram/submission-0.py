from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if sorted(s) == sorted(t):
        #     return True  
        # return False    

        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)    
