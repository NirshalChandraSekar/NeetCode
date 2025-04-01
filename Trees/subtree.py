# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root, subRoot) -> bool:
        def SameTree(p,q):
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

        if not subRoot:
            return True
        if not root:
            return False

        if SameTree(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
    
# Example usage
# Assuming TreeNode is defined as follows:
# Create a sample tree for testing
root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(0)
subRoot = TreeNode(4)
subRoot.left = TreeNode(1)
subRoot.right = TreeNode(2)
subRoot.right.left = TreeNode(0)
# Create an instance of the Solution class
solution = Solution()
# Call the isSubtree method and print the result
print(solution.isSubtree(root, subRoot))  # This will return True since the subtree matches