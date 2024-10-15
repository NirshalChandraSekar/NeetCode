class Solution:
    def searchMatrix(self, matrix, target):
        rows, columns = len(matrix), len(matrix[0])
        lower = 0
        upper = (rows * columns)-1

        while(lower <= upper):
            mid = lower + ((upper-lower)//2)
            r, c = (mid//columns), (mid%columns)
            
            if target > matrix[r][c]:
                lower = mid+1
            elif target < matrix[r][c]:
                upper = mid-1
            else:
                return True

        return False
    
if __name__ == '__main__':
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    obj = Solution()
    print(obj.searchMatrix(matrix, target))