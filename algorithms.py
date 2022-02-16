from elena import search 
from elena import Graph 
import copy

class BFS(search):
    # This is an iterative BFS algorithm that computes the shortest path between the source and target.
    def FindPath(self,u):
        while self.route:
            u = self.route[0]
            self.route.pop(0)
            for i in range(len(self.graph[u])):
                if (self.visit[self.graph[u][i]] == -1):
                    self.visit[self.graph[u][i]] = self.visit[u] + 1
                    self.path[self.graph[u][i]] = u
                    self.route.append(self.graph[u][i])
                    if (self.graph[u][i] == self.target):
                        path = []
                        crawl = self.target
                        path.append(crawl)                        
                        while (self.path[crawl] != -1):
                            path.insert(0,self.path[crawl])
                            crawl = self.path[crawl]
                        return path

        return []

class DFS(search):
    # This is an backtracking based method to compute the shortest path between  
    def FindPath(self,u):
        if u == self.target:
            if self.shortestDistance > self.visit[u]:
                self.shortestDistance = self.visit[u]
                self.path = copy.deepcopy(self.route)
            self.visit[u] = -1
            self.route.pop()
            return

        for i in range(len(self.graph[u])):
            if self.visit[self.graph[u][i]] == -1:
                self.visit[self.graph[u][i]] = self.visit[u] + 1
                self.route.append(self.graph[u][i])
                self.FindPath(self.graph[u][i])

        self.visit[u] = -1
        self.route.pop()