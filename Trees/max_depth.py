# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        max_depth = 1
        stack = [[root, 1]]
        while stack:
            list_ = stack.pop()
            node, ndepth = list_[0], list_[1]
            max_depth = ndepth if ndepth>max_depth else max_depth
            if node.left:
                stack.append([node.left, ndepth+1])
            if node.right:
                stack.append([node.right, ndepth+1])


        return max_depth
    
def print_tree(root):
    if not root:
        return
    print(root.val)
    print_tree(root.left)
    print_tree(root.right)

if __name__ == "__main__":
    s = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print("Original Tree:")
    print_tree(root)
    result = s.maxDepth(root)
    print("Max Depth:", result)