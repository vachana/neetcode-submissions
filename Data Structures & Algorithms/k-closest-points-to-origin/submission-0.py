import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res_points = []
        heap = []

        for point in points:
            x = point[0]
            y = point[1]
            dist = math.sqrt(pow(x, 2) + pow(y, 2))

            heapq.heappush(heap, (-dist, point))

            while len(heap) > k:
                heapq.heappop(heap)
            
        while heap:
            _, res = heapq.heappop(heap)
            res_points.append(res)

        return res_points

            