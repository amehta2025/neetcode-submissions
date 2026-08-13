# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max1 = 0
        def height(node):
            nonlocal max1
            if not node:
                return 0
            left = height(node.left)
            right = height(node.right)

            max1 = max(max1, left + right)

            return 1 + max(left,right) #keeps recursion going, finds height of tree

        height(root)
        return max1 

#define a function within a function
            

    

