class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        o_len = len(nums)
        nums = set(nums)
        if o_len == len(nums):
            return False
        return True