class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # cant use hashmap cuz it should be O(1), so We use array itself as a hash set without creating a new one. 

        for i in range(len(nums)):
            # idx is key-->nums = [1,2,3,2,2], map={0:1,1:2,2:3}
            idx = abs(nums[i]) - 1 #abs for the duplicate 

            if nums[idx] < 0:
                return abs(nums[i])

            nums[idx] *= -1 #marking the value(that idx/key as visited)


            
            
            
            
            
            

