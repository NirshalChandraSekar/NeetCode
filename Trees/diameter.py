# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root):
        max_dia = 0
        
        def find_dia(root):
            nonlocal max_dia
            if root is None:
                return 0

            left = find_dia(root.left)
            right = find_dia(root.right)

            max_dia = max(max_dia, left + right)

            return max(left,right) + 1

        find_dia(root)

        return max_dia
            

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
# Call the diameterOfBinaryTree method and print the result
print(solution.diameterOfBinaryTree(root))  # This will return 4 since the longest path is 4 -> 2 -> 1 -> 3
            