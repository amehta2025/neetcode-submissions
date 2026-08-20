class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x,y in points:
            distance = math.sqrt(x**2 + y**2)
            minHeap.append([distance, x, y])
        
        heapq.heapify(minHeap)
        j = 0
        ans = []
        while j < k:
            x,y,z = heapq.heappop(minHeap)
            ans.append([y,z])
            j+=1
        
        return ans