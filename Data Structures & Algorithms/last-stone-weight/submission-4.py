class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            val1 = -heapq.heappop(maxHeap)
            val2 = -heapq.heappop(maxHeap)
            if val1 > val2:
                heapq.heappush(maxHeap,-(val1-val2))
        
        if maxHeap:
            return -maxHeap[0]
        else:
            return 0

#use maxHeap, heappop 2 times to get the highest values