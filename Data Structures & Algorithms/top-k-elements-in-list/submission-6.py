class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_map = defaultdict(int)
        freq_map = [[] for _ in range(len(nums)+1)]
 
        res = []

        for n in nums:
            nums_map[n] = nums_map.get(n, 0) + 1

        for key, val in nums_map.items():
            # freq_map[val] = key --> No, cuz 2 numbers with same frequency will be overriden
            freq_map[val].append(key)

        for bucket in freq_map[::-1]:
            for val in bucket:
                res.append(val)
                k -= 1
                if k ==0:
                    return res


# BucketSort -> O(n) for both
# freq_map[::-1] to access values in reverse
# for i in range(len(freq_map) - 1, -1, -1):-> to access indices in reverse

# nums_map = defaultdict(int)
# nums_map["x"]  # key doesn't exist → returns 0 automatically
