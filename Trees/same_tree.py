# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p, q) -> bool:
        stack = [[p,q]]
        while stack:
            node1, node2 = stack.pop()
            
            if not node1 and not node2:
                continue

            if not node1 or not node2:
                return False

            if node1.val != node2.val:
                return False

            stack.append([node1.right, node2.right])
            stack.append([node1.left, node2.left])

        return True
    
# Example usage
# Assuming TreeNode is defined as follows:
# Create a sample tree for testing
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
# Create an instance of the Solution class
solution = Solution()
# Call the isSameTree method and print the result
print(solution.isSameTree(root1, root2))  # This will return True since both trees are the same