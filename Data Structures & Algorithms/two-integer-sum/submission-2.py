class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1. Brute Force
        # 2. Hash Map
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]