# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root):
        if root is None:
            return True

        check = None

        def height(root):
            nonlocal check
            if root is None:
                return 0

            left = height(root.left)
            right = height(root.right)

            if abs(left-right) > 1:
                check = False

            return max(left,right) + 1

        height(root)

        if check == False:
            return False
        else:
            return True
        
# Example usage
# Assuming TreeNode is defined as follows:
# Create a sample tree for testing
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
# Create an instance of the Solution class
solution = Solution()
# Call the isBalanced method and print the result
print(solution.isBalanced(root))  # This will return True since the tree is balanced
# Create an unbalanced tree for testing
root_unbalanced = TreeNode(1)
root_unbalanced.left = TreeNode(2)
root_unbalanced.left.left = TreeNode(3)
# Create an instance of the Solution class      
solution_unbalanced = Solution()
# Call the isBalanced method and print the result
print(solution_unbalanced.isBalanced(root_unbalanced))  # This will return False since the tree is unbalanced



