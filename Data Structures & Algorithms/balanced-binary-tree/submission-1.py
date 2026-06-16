# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True

        def dfs(root: TreeNode) -> int:
            nonlocal balanced

            if root == None:
                return 0
            if root.left == None and root.right == None:
                return 1
            
            leftH = dfs(root.left)
            rightH = dfs(root.right)

            if abs(leftH - rightH) > 1:
                balanced = False
            
            return max(leftH, rightH) + 1
        
        dfs(root)
        return balanced