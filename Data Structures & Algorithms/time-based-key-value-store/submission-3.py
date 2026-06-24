class TimeMap:

    def __init__(self):
        self.timestamp = defaultdict(list)
        
# TC: O(1) and SC: O(n)
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timestamp[key].append((timestamp, value))

# TC: O(logn) and SC: O(1)
# It's timestamp, so already ordered list, use binary search
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.timestamp[key]
        l = 0
        r = len(values) - 1

        while l <= r:
            mid = (l + r)//2
            if timestamp >= values[mid][0]:
                res = values[mid][1]
                l +=1
            else:
                r -=1
        
        return res


        
