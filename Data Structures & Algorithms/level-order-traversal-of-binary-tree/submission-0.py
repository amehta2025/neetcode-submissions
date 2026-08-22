# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        q = collections.deque()
        q.append(root)
        while q:
            length = len(q)
            row = []
            for _ in range(length):
                curr = q.popleft()
                row.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(row)
        
        return res


            
            


#this is literally the definition of BFS
#i'd prolly review this again; example of BFS without recursion