import math

class Solution:
    def maxArea(self, heights):
        max_area = 0
        i = 0
        j = len(heights)-1
        while(i<j):
            area = (j - i) * (min(heights[i],heights[j]))
            if(area>max_area):
                max_area = area
            else:
                if(heights[i]>heights[j]):
                    j -= 1
                elif(heights[i]<heights[j]):
                    i += 1
                else:
                    i += 1

        return max_area
        
if __name__ == "__main__":
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7])) #Output: 49
    print(s.maxArea([1,1])) #Output: 1
    print(s.maxArea([4,3,2,1,4])) #Output: 16
    print(s.maxArea([1,2,1])) #Output: 2
    print(s.maxArea([1,2,4,3])) #Output: 4