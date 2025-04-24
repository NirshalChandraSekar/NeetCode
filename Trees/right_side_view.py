# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root):
        final_list = []
        level = 0
        stack = [[level, root]]
        while stack:
            level_, node = stack.pop()
            if node:
                if level_ < len(final_list):
                    final_list[level_] = node.val

                else:
                    final_list.append(node.val)

                if node.right:
                    stack.append([level_+1, node.right])
                if node.left:
                    stack.append([level_+1, node.left])

        return final_list
    
# Example usage:
# Constructing a sample binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
solution = Solution()
right_side_view = solution.rightSideView(root)
print(right_side_view)  # Output: [1, 3, 7]     
