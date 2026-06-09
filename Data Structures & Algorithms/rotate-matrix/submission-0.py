class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        left, right = 0, n-1

        # reverse the matrix(flip rows) 
        # there is an in-build function at O(1)->matrix.reverse()
        while left < right:
            matrix[left], matrix[right] = matrix[right], matrix[left]
            left +=1
            right -=1
        

        # Transpose
        for i in range(n):
            for j in range(i+1, n): #only upper triangle, otherwise ul reflip to original
                matrix[i][j],matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # TC:O(n2), SC O(1)
            

        

        
