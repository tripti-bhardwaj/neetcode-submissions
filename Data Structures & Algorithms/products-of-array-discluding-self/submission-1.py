class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = [1] * len(nums)
        prefix = postfix = 1
        for i in range(len(nums)):
            product[i] = prefix
            prefix *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
            product[i] *= postfix
            postfix *= nums[i]
        return product

