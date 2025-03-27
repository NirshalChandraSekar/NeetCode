class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root):
        stack = [[root, 1]]
        max_depth = 0
        
        while stack:
            node, depth = stack.pop()
            if max_depth < depth:
                max_depth = depth
            if node.left:
                stack.append([node.left, depth+1])
            if node.right:
                stack.append([node.right, depth+1])
        return max_depth

# example usage
# Assuming TreeNode is defined as follows:

# Create a sample tree for testing
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
# Create an instance of the Solution class
solution = Solution()
# Call the maxDepth method and print the result
# This will print the depth of each node as it is traversed
print(solution.maxDepth(root))  # This will print the depth of each node as it is traversed
        

