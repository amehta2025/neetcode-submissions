class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-n for n in nums]
        heapq.heapify(maxHeap)
        
        num = 0
        while k > 0:
            num = -heapq.heappop(maxHeap)
            k-=1
        
        return num
            