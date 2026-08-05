class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)

        bucket = [[] for _ in range(len(nums))]
        for key, value in counts.items():
            bucket[value-1].append(key)
        
        res = []
        for i in range(len(bucket)-1, -1, -1):
            for j in range(0, len(bucket[i])):
                res.append(bucket[i][j])
                k -= 1
                if k <= 0:
                    return res

        return res