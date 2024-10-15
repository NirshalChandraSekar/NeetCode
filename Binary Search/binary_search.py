class Solution:
    def search(self, nums, target):
        index = -1
        lower, upper = 0, len(nums)-1
        
        while(lower<=upper):
            mid = lower + ((upper-lower)//2)

            if target > nums[mid]:
                lower = mid+1
            elif target < nums[mid]:
                upper = mid-1
            else:
                return mid

        return index
    
if __name__ == '__main__':
    nums = [-1,0,3,5,9,12]
    target = 9
    obj = Solution()
    print(obj.search(nums, target))