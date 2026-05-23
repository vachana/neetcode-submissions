class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 1
        set_s = set()
        res = 0
        for r in range(len(s)):
            while s[r] in set_s:
                set_s.remove(s[l])
                l +=1
            set_s.add(s[r])
            res = max(res, len(set_s)) # or window size i.e (r-l+1)

        return res

# O(n) for both

