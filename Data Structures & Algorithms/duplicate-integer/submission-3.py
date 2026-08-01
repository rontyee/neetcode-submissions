class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for num in nums:
            if num not in d:
                d[num] = True
            else:
                return True
        return False