class Solution:
    def evalRPN(self, tokens):
        stack = []
        for i in tokens:
            if i == "+":
                first = stack.pop()
                second = stack.pop()
                stack.append(first+second)

            elif i == "-":
                first = stack.pop()
                second = stack.pop()
                stack.append(second-first)

            elif i == "*":
                first = stack.pop()
                second = stack.pop()
                stack.append(first*second)

            elif i == "/":
                first = stack.pop()
                second = stack.pop()
                stack.append(int(float(second)/first))
            
            else:
                stack.append(int(i))

        return stack[-1]
            

if __name__ == '__main__':
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    obj = Solution()
    print(obj.evalRPN(tokens))