class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_val = 1
        max_val = max(piles)
        temp = max_val

        while min_val <= max_val:
            mid = min_val + (max_val-min_val)//2
            num_hours = 0
            for bananas in piles:
                num_hours += math.ceil(bananas/mid)
            
            if num_hours <= h:
                max_val = mid - 1
                temp = mid
            elif num_hours > h:
                min_val = mid + 1
        
        return temp