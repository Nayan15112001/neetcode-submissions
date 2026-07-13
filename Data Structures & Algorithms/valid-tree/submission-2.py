class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list =  {}
        visiting = set()
        done = set()

        if len(edges)!=n-1:
            return False

        for i in range(n):
            adj_list[i] = []

        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])

        print(adj_list)

        def dfs(k,parent):
            if k in visiting:
                return False
            if k in done:
                return True
            
            visiting.add(k)
            for nei in adj_list[k]:
                if nei == parent:
                    continue
                elif not dfs(nei,k):
                    return False
            
            visiting.remove(k)
            done.add(k)
            return True




        if not dfs(0,0):
            return False
        
        if len(done) != n:
            return False
        return True

