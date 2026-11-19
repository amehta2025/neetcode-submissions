from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        indegrees = [0] * numCourses
        visited = set()
        order = []
        for i,j in prerequisites:
            adj_list[j].append(i)
            indegrees[i] +=1
        
        q = deque()
        for idx, val in enumerate(indegrees):
            if val == 0:
                q.append(idx)
                visited.add(idx)
        
        while q:
            course = q.popleft()
            order.append(course)
            for c in adj_list[course]:
                indegrees[c]-=1
                if indegrees[c] == 0 and c not in visited:
                    q.append(c)
                    visited.add(c)

        if len(order) < numCourses:
            return []
        return order
        
