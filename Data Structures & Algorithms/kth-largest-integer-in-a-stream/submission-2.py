class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > self.k:   #remove from root (smallest) so you're left with k largest
            heapq.heappop(self.minHeap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        while len(self.minHeap) > self.k:   #remove from root (smallest) so you're left with k largest
            heapq.heappop(self.minHeap)
        return self.minHeap[0]


#adding with a heap is O(log(n)),  adding with binary search is adding in the middle of an array which is O(n)