class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        res = []
        for x,y in points:
            minHeap.append((math.sqrt(x **2 + y**2),x,y))
        heapq.heapify(minHeap)
        for i in range(k):
            tup = heapq.heappop(minHeap)
            res.append((tup[1], tup[2]))
        
        return res