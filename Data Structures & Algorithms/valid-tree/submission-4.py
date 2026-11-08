from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        visited = set()
        for i,j in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)
        
        q = deque()
        q.append((0,-1))  #choose 0 to be the starting root of the tree

        while q:
            val,parent = q.popleft()
            if val in visited:
                return False
            visited.add(val)
            for i in adj_list[val]:
                if i == parent:
                    continue
                q.append((i, val))
            
        
        return n == len(visited) #it could be that all of the nodes are not connected
                

