class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Solution1: Sorting->TC is O(m*nlogn)

        # res = defaultdict(list)
        # here values of dict are a list

        # for s in strs:
        #     sorted_s = ''.join(sorted(s))
        #     res[sorted_s].append(s)
        # return list(res.values())

        # Solution 2: Hashmap TC and SC O(m*n)
        res = defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord('z') - ord(c)] += 1
            res[tuple(count)].append(s)
            # Lists are mutable.Mutable objects cannot
            # be dictionary keys.Tuple is immutable
        return list(res.values())



        # Count frequency of each element in a group
        # Use that frequency representation as a key
        # Group items that share the same key





