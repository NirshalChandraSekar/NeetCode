class Solution:
    def isValid(self, s: str) -> bool:
        hash_table = {")": "(", "]": "[", "}": "{"}
        stack = []
        
        for i in s:
            if i not in hash_table:
                stack.append(i)
            else:
                if not stack or hash_table[i] != stack[-1]:
                    return False
                stack.pop()
        
        return len(stack) == 0
    
if __name__ == "__main__":
    s = Solution()
    print(s.isValid("()"))
    print(s.isValid("()[]{}"))
    print(s.isValid("(]"))
    print(s.isValid("([)]"))
    print(s.isValid("{[]}"))
    print(s.isValid("]"))
    print(s.isValid("["))
    print(s.isValid("]"))
    print(s.isValid("(("))
