# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import math
class Solution:
    def isValidBST(self, root):
        if not root:
            return True

        left_boundary = -math.inf
        right_boundary = math.inf

        stack = [[root, left_boundary, right_boundary]]
        
        while stack:
            node, left, right = stack.pop()
            
            if node.val <= left or node.val >= right:
                return False

            if node.left:
                stack.append([node.left, left, node.val])
            
            if node.right:
                stack.append([node.right, node.val, right])

        return True
    
# Example usage:
# Constructing a sample binary tree root=[2,1,3]
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
solution = Solution()
is_valid_bst = solution.isValidBST(root)
print(is_valid_bst)  # Output: True
# Constructing a sample binary tree root=[5,1,4,null,null,3,6]
root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(6)
solution = Solution()
is_valid_bst = solution.isValidBST(root)
print(is_valid_bst)  # Output: False