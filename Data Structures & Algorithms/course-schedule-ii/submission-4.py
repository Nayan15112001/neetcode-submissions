class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        adj_list = {}
        seen = set()
        done = []
        #building the adj list
        for i in range(numCourses):
            adj_list[i] = []
        for prereq in prerequisites:
            adj_list[prereq[0]].append(prereq[1])

        def dfs(k):
            #base condition

            if k in seen:
                return False
            if k in done:
                return True
            
            seen.add(k)
            for val in adj_list[k]:
                if not dfs(val):
                    return False
            
            seen.remove(k)
            done.append(k)

            return True


        for k,v in adj_list.items():
            if not dfs(k):
                return []

        # if len(done) == numCourses:
        #     return done
        # else:
        #     return []

        return done
