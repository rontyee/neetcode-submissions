class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, n in enumerate(nums):
            possible_sum = target - n
            if possible_sum in hash_map:
                return [hash_map[possible_sum], i]
            else:
                hash_map[n] = i

