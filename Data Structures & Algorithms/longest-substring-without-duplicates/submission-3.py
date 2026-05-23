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
            res = max(res, len(set_s))

            
        return res

# s="pwwkew"
# l =0, r=1, temp = 2, res = 1
# l =0, r=1, temp = 3, res = 1

