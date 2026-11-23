class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # 1. Brute Force Done
        # 2. Sorting
        # 3. Hash Set
        # 4. Set Length
        # 5. Hash Map
        return len(set(nums)) < len(nums)



