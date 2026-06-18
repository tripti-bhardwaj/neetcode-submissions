class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        min_element = nums[low]
        while low <= high:
            mid = low + (high-low) // 2
            min_element = min(min_element, nums[mid])
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid - 1
        return min_element