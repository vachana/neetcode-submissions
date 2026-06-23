class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # graph = defaultdict(list)

        # for u, v in prerequisites:
        #     graph[u].append(v) 

        # for k, v in graph.items():
        #     for node in v:
        #         if node in graph and k in graph[node]:
        #             return False

        # return True    
        # The above wont work for this kind of cycle->prerequisites=[[1,0],[0,2],[2,1]]
        # It'l only work for [[0,1],[1,0]]  

        graph = defaultdict(list)

        for u, v in prerequisites:
            graph[u].append(v)
        
        visiting = set()
        visited = set()

        def dfs(node):
            if node in visiting:
                return False

            if node in visited:
                return True
            
            visiting.add(node)

            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
                
            visiting.remove(node)
            visited.add(node)
            return True


        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

