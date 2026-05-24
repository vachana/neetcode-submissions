class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freq = {}
        max_freq =0
        res = 0

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r],0) + 1
            max_freq = max(max_freq, freq[s[r]])
            if (r-l+1) - max_freq > k:
                freq[s[l]] -=1
                l +=1
            res = max(res, r-l+1)#window size each time

        return res

# O(n)->TC
# O(1)->SC  at most 26 keys (only uppercase English chars)