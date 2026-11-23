class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1. Sorting
        # 2. Hash Map
        # 3. Counter
        # 4. Array
        # 5. Hybrid Map
        if len(s) != len(t):
            return False
        arr = [0] * 26
        for i in range(len(s)):
            arr[ord(s[i]) - ord('a')] += 1
            arr[ord(t[i]) - ord('a')] -= 1
        for i in range(len(arr)):
            if arr[i] != 0:
                return False
        return True
        