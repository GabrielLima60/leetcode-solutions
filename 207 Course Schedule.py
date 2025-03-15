'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
'''

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        nodes = {}
        self.answer = True
        self.visiting = set()
        self.visited = set()

        for duple in prerequisites:
            if duple[0] not in nodes:
                nodes[duple[0]] = [duple[1]]
            else:
                nodes[duple[0]].append(duple[1])

        for course in nodes:
            self.dfs(course, nodes)

        return self.answer

    
    def dfs(self, course, nodes):
        if course in self.visited:
            return 
        if course in self.visiting:
            self.answer = False

        else:
            self.visiting.add(course)
            for dependency in nodes[course]:
                if dependency in nodes:
                    self.dfs(dependency, nodes)
            self.visiting.remove(course)
            self.visited.add(course)
