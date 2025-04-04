# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        
        while root:
            if p.val > root.val and q.val > root.val:
                root = root.right

            elif p.val < root.val and q.val < root.val:
                root = root.left

            else:
                return root
            
# Example usage:
# Constructing a sample BST
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
p = root.left  # Node with value 2
q = root.left.right  # Node with value 4
solution = Solution()
lca = solution.lowestCommonAncestor(root, p, q)
print(lca.val)  # Output: 2