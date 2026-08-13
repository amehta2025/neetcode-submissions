class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = stones;
        maxHeap = [-s for s in maxHeap]
        heapq.heapify(maxHeap)  #maxHeap, so heapify afterwards
        while len(maxHeap) > 1:
            num1 = -heapq.heappop(maxHeap) # assign it to this so the heap decides which values to put
            num2 = -heapq.heappop(maxHeap)
        
            if (num1 > num2): # [6, 4, 3, ...]
                heapq.heappush(maxHeap, -(num1-num2))
        if maxHeap:
            return -maxHeap[0]

        return 0