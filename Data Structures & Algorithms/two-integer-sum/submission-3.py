class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1. Brute Force
        # 2. Hash Map
        h = {}
        for i in range(len(nums)):
            num = nums[i]
            needed = target - num
            if needed in h:
                return [h[needed], i]
            h[num] = i