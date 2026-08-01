class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
    
        hx, hy = {}, {}

        for i in range(len(s)):
            hx[s[i]] = 1 + hx.get(s[i], 0)
            hy[t[i]] = 1 + hy.get(t[i], 0)

        if hx == hy:
            return True
        return False