# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    count = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.height(root)
        return self.count
    
    def height(self, root: TreeNode) -> int:
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        
        leftH = self.height(root.left)
        rightH = self.height(root.right)

        if  leftH + rightH > self.count:
            self.count = leftH + rightH

        return max(leftH, rightH) + 1