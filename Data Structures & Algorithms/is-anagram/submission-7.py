class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1. Sorting
        # 2. Hash Map
        # 3. Counter
        # 4. Array
        # 5. Hybrid Map
        if len(s) != len(t):
            return False
        s_hash = {}
        t_hash = {}

        for i in range(len(s)):
            s_hash[s[i]] = 1 + s_hash.get(s[i], 0)
            t_hash[t[i]] = 1 + t_hash.get(t[i], 0)
        for i in range(len(s)):
            if s_hash[s[i]] != t_hash.get(s[i], 0):
                return False
        return True
