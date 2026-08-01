class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_sum = [1] * n
        postfix_sum = [1] * n
        res = [1] * n
        for i in range(1,n):
            prefix_sum[i] = prefix_sum[i-1] * nums[i-1]
        for i in range(n - 2, -1, -1):
            postfix_sum[i] = postfix_sum[i+1] * nums[i+1]
        for i in range(n):
            res[i] = prefix_sum[i] * postfix_sum[i]
        return res
        