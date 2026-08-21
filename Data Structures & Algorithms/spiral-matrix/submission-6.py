class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        top = 0 
        right = n-1
        bottom = m-1
        left = 0
        res =[]
        while top <=  bottom and left <= right:
            for j in range(left,right+1):
                res.append(matrix[top][j])
            top +=1
            for i in range(top,bottom+1):
                res.append(matrix[i][right])
            right -=1  
            if not (top <= bottom and left <= right):
                break
            for j in range(right,left-1,-1):
                res.append(matrix[bottom][j])
            bottom -= 1
            for i in range(bottom,top-1,-1):
                res.append(matrix[i][left])
            left += 1
        return res      