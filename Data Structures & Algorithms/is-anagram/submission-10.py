class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1. Sorting
        # 2. Hash Map
        # 3. Counter
        # 4. Array
        # 5. Hybrid Map
        if len(s) != len(t):
            return False
        h = {}
        for i in range(len(s)):
            h[s[i]] = h.get(s[i], 0) + 1
            h[t[i]] = h.get(t[i], 0) - 1
        for i in h:
            if h[i] != 0:
                return False
        return True