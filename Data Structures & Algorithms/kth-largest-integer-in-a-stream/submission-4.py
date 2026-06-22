import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.heap = []
        for n in nums:
            heapq.heappush(self.heap, n)
            if len(self.heap) > self.k:
                heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
                heapq.heappop(self.heap)


        return self.heap[0]

# Since heap size never grows beyond k + 1, each operation is based on k, not full n.
#  COnstructor: TC:      O(log k).  SC: O(k)
# Add: TC: O(log k) SC:O(1) extra
            
