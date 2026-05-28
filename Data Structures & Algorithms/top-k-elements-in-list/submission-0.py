from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)
        for num in nums:  
            frequency[num] += 1

        sorted_nums = sorted(frequency, key = frequency.get, reverse = True)
        
        return sorted_nums[:k]
