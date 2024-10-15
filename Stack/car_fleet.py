class Solution:
    def carFleet(self, target, position, speed):
        combined = [(x,y) for x,y in zip(position, speed)]
        combined.sort(reverse=True)
        stack = []
        for pos, speed in combined:
            stack.append((target-pos)/speed)
            if len(stack)>=2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)


if __name__ == '__main__':
    target = 12
    position = [10,8,0,5,3]
    speed = [2,4,1,1,3]
    obj = Solution()
    print(obj.carFleet(target, position, speed))