class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for n in nums:
            if (n - 1) not in nums_set:
                #it is a starting secquence
                seq_count = 1
                while (n + seq_count) in nums_set:
                    seq_count += 1
                longest = max(longest, seq_count)

        return longest