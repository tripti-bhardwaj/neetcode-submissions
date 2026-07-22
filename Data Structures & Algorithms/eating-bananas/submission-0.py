class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) <= h:
            low, high = 1, max(piles)
            result = high
            while low <= high:
                mid = low + (high - low) // 2
                hours = 0
                for p in piles:
                    hours += math.ceil(p/mid)
                if hours <= h:
                    result = min(result, mid)
                    high = mid - 1
                else:
                    low = mid + 1
        return result