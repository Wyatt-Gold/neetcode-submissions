class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1
        
        heap = []
        for num in freqs:
            freq = freqs[num]
            if(len(heap) >= k):
                if heap[0][0] < freq:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (freq, num))
            else:
                heapq.heappush(heap, (freq, num))
        
        res = []
        for num in heap:
            res.append(num[1])
        
        return res