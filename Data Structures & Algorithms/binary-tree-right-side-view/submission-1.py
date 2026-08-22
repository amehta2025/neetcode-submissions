# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        q = deque()
        q.append(root)
        res.append(root.val)
        while q:
            length = len(q)
            curr = []
            for _ in range(length):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                    curr.append(node.left.val)
                if node.right:
                    q.append(node.right)
                    curr.append(node.right.val)
            
            if curr:
                res.append(curr[-1])

        return res
        