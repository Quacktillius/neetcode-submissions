# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        answer = float('-inf')

        def dfs(root: TreeNode) -> int:
            nonlocal answer

            if root == None:
                
                return 0
            if root.left == None and root.right == None:
                if root.val > answer:
                        answer = root.val
                return root.val
            
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            
            answerIncludingRootAndBothLR = max(max(root.val, root.val + max(leftMax, rightMax)), root.val + leftMax + rightMax)
            if answerIncludingRootAndBothLR > answer:
                answer = answerIncludingRootAndBothLR
            answerWithOnlyOnseSide = max(root.val, root.val + max(leftMax, rightMax))
            return answerWithOnlyOnseSide
        
        dfs(root)
        return answer