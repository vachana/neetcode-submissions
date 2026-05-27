class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_count, t_count = {}, {}

        for i in range(len(s)):
            s_count[s[i]] = s_count.get(s[i], 0) + 1 
            t_count[t[i]] = t_count.get(t[i], 0) + 1 

        return s_count == t_count   























        # if len(s) != len(t):
        #     return False

        # s_count, t_count = {}, {} 

        # # After adding the length comparisn above(line 3)
        # # U can merge the 2 for loops
        # for c in s:
        #     s_count[c] = 1 + s_count.get(c, 0)

        # for c in t:
        #     t_count[c] = 1 + t_count.get(c, 0)
        
        # return s_count == t_count

        # # by usingHashmap/dict
        # # O(1) for SC as it's atmost 26characters
        # # O(n + m) for TC when n= len(s) and m= len(t)