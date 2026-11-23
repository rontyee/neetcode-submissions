class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1. Sorting
        # 2. Hash Map
        # 3. Counter
        # 4. Array
        # 5. Hybrid Map
        return Counter(s) == Counter(t)