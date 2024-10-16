import math
class Solution:
    def minEatingSpeed(self, piles,h):
        k = math.inf
        piles.sort()
        lower = 1
        upper = max(piles)
        while(lower<=upper):
            mid = (lower + upper)//2
            hours = 0
            for p in piles:
                hours += math.ceil(p/mid)
            if hours <= h:
                upper = mid-1
                if mid<k:
                    k=mid
            else:
                lower = mid+1
        return k
    
if __name__ == '__main__':
    piles = [3,6,7,11]
    h = 8
    obj = Solution()
    print(obj.minEatingSpeed(piles, h))