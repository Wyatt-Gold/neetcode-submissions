class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []

        for i in range(0, len(points)):
            x, y, = points[i][0], points[i][1]
            dist = math.sqrt(pow(x-0,2) + pow((y-0),2))
            heapq.heappush(heap, (dist, i))
        
        while k > 0:
            res.append(points[heapq.heappop(heap)[1]])
            k -= 1
        
        return res