class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # carry = 1
        # res =[]

        # for i in range(len(digits)-1, -1, -1):
        #     digit = digits[i] + carry
        #     res.append(digit % 10)
        #     carry = digit // 10
        #     # if u do n = digit% 10 and then res = res*10+n ,then res=01 instead of 0001
        
        # if carry == 1:
        #     res.append(1)
        
        # return res[::-1]
        # # O(n) for TC and SC

        # for O(1) SC, modify [digits]
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] =0
        
        return [1] + digits


            
            


        
        
           