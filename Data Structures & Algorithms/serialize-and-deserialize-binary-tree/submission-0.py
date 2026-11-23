# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        
        q = deque()
        q.append(root)
        res = ""
        res += str(root.val) + ","

        while q:
            for i in range(len(q)):
                n = q.popleft()
                if n.left == None:
                    res+="null,"
                else:
                    res+= str(n.left.val) + ","
                    q.append(n.left)

                if n.right == None:
                    res+="null,"
                else:
                    res+= str(n.right.val) + ","
                    q.append(n.right)
        
        return res

  
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None
        
        order = data.split(",")
        
        root = TreeNode(int(order[0]))
        q = deque()
        q.append(root)
        idx = 1
        while q:
            n = q.popleft()
            if order[idx] != "null":
                n.left = TreeNode(int(order[idx]))
                q.append(n.left)
            idx+=1
            if order[idx] != "null":
                n.right = TreeNode(int(order[idx]))
                q.append(n.right)
            
            idx+=1
        
        return root


            




