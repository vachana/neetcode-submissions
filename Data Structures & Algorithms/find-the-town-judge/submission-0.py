class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming_edges = defaultdict(int)
        outgoing_edges = defaultdict(int)

        for src, dest in trust:
            incoming_edges[dest] +=1
            outgoing_edges[src] +=1
        
        for i in range(1, n+1):
            if incoming_edges[i] == n-1 and outgoing_edges[i] == 0:
                return i
        return -1

        # O(V+E) TC
        # SC O(V)
        