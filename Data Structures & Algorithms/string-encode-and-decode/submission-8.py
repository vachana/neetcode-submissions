class Solution:
# Encoding is about representation, encryption is about protection.
# Safe transmission (networks, files)
# Compatibility (binary → text)
# Serialization (like your Encode/Decode Strings problem)

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s

        return res

# += creates a new string each time which is technically O(n²).so do
# return "".join(str(len(s)) + "#" + s for s in strs)  # O(n)

    def decode(self, s: str) -> List[str]:
        res = []

        l = 0

        while l < len(s):
            count = ""
            len_c = 0
            while s[l] != "#":
                count += s[l]
                l +=1
            l +=1

            len_c = int(count)
            res.append(s[l:l+len_c])
            l += len_c
        return res

# O(n) for both










    # def encode(self, strs: List[str]) -> str:
    #     encoded = ""
    #     for s in strs:
    #         len_s = str(len(s))
    #         encoded = encoded + len_s + "#" + s
    #     return encoded

    # def decode(self, s: str) -> List[str]:
    #     decoded= []
    #     i=0

    #     while i < len(s):
    #         len_s = ""
    #         while s[i]!= "#":
    #             # this is for numbers above 9
    #             len_s += s[i]
    #             # or use another variable 'j' to
    #             # increment and use as index instead of concatinating len_s
    #             i +=1
    #         each_str = s[i+1: i+1+int(len_s)]
    #         decoded.append(each_str)
    #         i = i+1+int(len_s)
        
    #     return decoded


    #     

            



            





