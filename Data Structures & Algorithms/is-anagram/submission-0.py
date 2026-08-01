class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_map = {}
        t_map = {}
        s_set = set(s)
        t_set = set(t)

        if s_set != t_set:
                return False

        for ch in s:
            if ch not in s_map:
                s_map[ch] = 0
            else:
                s_map[ch] += 1
        
        for ch in t:
            if ch not in t_map:
                t_map[ch] = 0
            else:
                t_map[ch] += 1

        for ch in s_set:
            if s_map[ch] != t_map[ch]:
                return False

        return True

        