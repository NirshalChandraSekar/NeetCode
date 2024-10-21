class Solution:
    def search(self, nums, target):
        lower = 0
        upper = len(nums)-1

        while(lower<=upper):
            mid = (lower + upper)//2

            if target == nums[mid]:
                return mid

            if nums[mid] <= nums[upper]: # its on the right side of the list
                if target < nums[mid] or target > nums[upper]:
                    upper = mid-1

                else:
                    lower = mid+1

            else:
                if target < nums[mid] and target > nums[upper]:
                    upper = mid-1
                else:
                    lower = mid+1

        return -1

if __name__ == '__main__':
    obj = Solution()
    print(obj.search([4,5,6,7,0,1,2],0))
    print(obj.search([4,5,6,7,0,1,2],3))
  