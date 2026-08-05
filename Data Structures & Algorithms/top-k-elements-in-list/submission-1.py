class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        counts = {}

        for num in nums:
            counts[num] = 1 + counts.get(num, 0)
        counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))

        for key in counts:
            res.append(key)
            k -= 1
            if k <= 0:
                break
        return res