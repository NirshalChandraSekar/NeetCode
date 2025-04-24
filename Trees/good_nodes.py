# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root):
        
        good_nodes = 0

        if not root:
            return good_nodes

        


        stack = [[root,[]]]
        
        while stack:
            node, node_list = stack.pop()
            
            current_list = node_list + [node.val]

            if node.val >= max(current_list):
                good_nodes += 1

            if node.right:
                stack.append([node.right, current_list])

            if node.left:
                stack.append([node.left, current_list])

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

            
