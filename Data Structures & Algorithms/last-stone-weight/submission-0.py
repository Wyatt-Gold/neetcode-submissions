class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -1 * stone)

        while len(heap) > 1:
            y = -1 * heapq.heappop(heap)
            x = -1 * heapq.heappop(heap)
            if y - x > 0:
                heapq.heappush(heap, -1 * (y - x))
        
        if heap:
            return -1 * heap[0]
        return 0