class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            difference = target - numbers[i]
            if difference in numbers:
                return [i + 1, numbers.index(difference) + 1]