class Solution:
    def isAnagram (self,s:str,t:str) -> bool:
        counte_s = Counter(s)
        counte_t = Counter(t)

        return counte_s == counte_t
