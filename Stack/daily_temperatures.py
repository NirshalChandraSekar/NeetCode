class Solution:
    def dailyTemperatures(self, temperatures):
        results = []
        i = 0
        j = i+1
        while(i<len(temperatures)-1):
            if j < len(temperatures) and temperatures[j] > temperatures[i]:
                results.append(j-i)
                i+=1
                j = i+1
            elif j<len(temperatures):
                j+=1
            else:
                results.append(0)
                i+=1
                j = i+1
        results.append(0)
        return results
    
if __name__ == '__main__':
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    obj = Solution()
    print(obj.dailyTemperatures(temperatures))