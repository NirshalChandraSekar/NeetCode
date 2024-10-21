class Solution:
    def findMin(self, nums):
        start , end = 0, len(nums) - 1 
        curr_min = float("inf")
        
        while start  <  end :
            mid = start + (end - start ) // 2
            curr_min = min(curr_min,nums[mid])
            
            # right has the min 
            if nums[mid] > nums[end]:
                start = mid + 1
                
            # left has the  min 
            else:
                end = mid - 1 
                
        return min(curr_min,nums[start])
    
if __name__ == '__main__':
    obj = Solution()
    print(obj.findMin([3,4,5,1,2]))
    print(obj.findMin([4,5,6,7,0,1,2]))
    print(obj.findMin([11,13,15,17]))
    print(obj.findMin([2,1]))
    print(obj.findMin([2,3,4,5,1]))