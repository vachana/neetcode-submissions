class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_dict, t_dict = {}, {}


        
        for i in range(len(s)):
            s_dict[s[i]] = s_dict.get(s[i], 0 ) + 1
            t_dict[t[i]] = t_dict.get(t[i], 0 ) + 1
        
        return s_dict == t_dict


        # by usingHashmap/dict
        # O(1) for SC as it's atmost 26characters
        # O(n + m) for TC when n= len(s) and m= len(t)