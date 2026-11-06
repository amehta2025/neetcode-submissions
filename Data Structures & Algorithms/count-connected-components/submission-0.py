class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        res = n
        for u,v in edges:
            res-=dsu.union(u,v)
        
        return res

class DSU:
    def __init__(self,n):
        self.parents = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self,node): #finds the root parent
        curr = node
        while curr != self.parents[curr]:
            self.parents[curr] = self.parents[self.parents[curr]] #path compression (optional line)
            curr = self.parents[curr];
        return curr
    
    def union(self, n1, n2): #combines 2 nodoes into the same group(along with nodes its connected to)
        p1 = self.find(n1)
        p2 = self.find(n2)
        if p1 == p2:
            return 0
        if self.rank[p1] > self.rank[p2]: 
            self.parents[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parents[p1] = p2
            self.rank[p2] += self.rank[p1]
        return 1


