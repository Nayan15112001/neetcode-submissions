class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = {}
        visited = set()
        count = 0

        for i in range(n):
            adj_list[i] = []

        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
        
        def dfs(k):
            if k in visited:
                return False
            
            visited.add(k)
            for val in adj_list[k]:
                if val in visited:
                    continue
                elif not dfs(val):
                    return False
            

            return True
                    




        for k,v in adj_list.items():
            if k in visited:
                continue
            elif dfs(k):
                count+=1
            
        return count
