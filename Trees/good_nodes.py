# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        good_nodes = 0

        if not root:
            return good_nodes

        stack = [[root, root.val]]
        
        while stack:
            root, max_history = stack.pop()
            # current_list.append(root.val)

            max_val = max(root.val, max_history)
            
            if root.val >= max_val:
                good_nodes += 1

            if root.left:
                stack.append([root.left, max_val])

            if root.right:
                stack.append([root.right, max_val])

        return good_nodes
            

# Example usage:
# Constructing a sample binary tree root=[2,1,1,3,null,1,5]
root = TreeNode(2)
root.left = TreeNode(1)     
root.right = TreeNode(1)
root.left.left = TreeNode(3)
root.left.right = None
root.right.left = TreeNode(1)
root.right.right = TreeNode(5)
solution = Solution()
good_nodes = solution.goodNodes(root)
print(good_nodes)  # Output: 4
# Constructing a sample binary tree root=[3,1,4,3,null,1,5]

            
