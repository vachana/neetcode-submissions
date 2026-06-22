import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res_points = []
        max_heap = []

        for point in points:
            x = point[0]
            y = point[1]
            dist = math.sqrt(pow(x, 2) + pow(y, 2))

            heapq.heappush(max_heap, (-dist, point))

            while len(max_heap) > k:
                heapq.heappop(max_heap)
            
        while max_heap:
            _, res = heapq.heappop(max_heap)
            res_points.append(res)

        return res_points

# | Complexity |        Value | where, n = len(points)k = number of closest points needed
# | ---------- | -----------: |
# | Time       | `O(n log k)` |
# | Space      |       `O(k)` |
