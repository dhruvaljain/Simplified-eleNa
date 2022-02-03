import random


class Graph():

    def __init__(self, algo):
        if algo == "BFS":
            self.N = 10000
        else:
            self.N = 10
        self.EDGE_LIMIT = 10
        self.algo = algo
        self.graph = self.generate_graph()

    def generate_graph(self):
        graph = [[]]
        num_edges = [random.randrange(0, self.EDGE_LIMIT, 1) for i in range(self.N)]        
        for edge in num_edges:
            graph.append([random.randrange(1, self.N+1, 1) for i in range(edge)])
        return graph
        # print(self.graph)
    
class search():
    def __init__(self,source, target, algo):
        self.graph = Graph(algo).graph
        # self.graph = [[],[2,4],[3],[5],[5],[6],[]]
        self.src = source
        self.target = target
        if algo == "DFS":
            self.path = [self.src]
            self.shortestDistance = 1000
        else:
            self.path = [-1]*len(self.graph)
        self.route = [self.src]
        self.visit = [-1]*len(self.graph)
        self.visit[self.src] = 0
    
    def FindPath(self):
        pass




    

# x = BFS(1,6,"BFS")
# print(x.FindPath(1))




# print(x.src)
# def FindPath(self):
#     print(self.graph)
#     visit = [-1]*len(self.graph)
#     visit[self.src] = 0
#     q = [self.src]
#     pred = [-1]*len(self.graph)
#     while q:
#         u = q[0]
#         q.pop(0)
#         for i in range(len(self.graph[u])):
#             if (visit[self.graph[u][i]] == -1):
#                 visit[self.graph[u][i]] = visit[u] + 1
#                 pred[self.graph[u][i]] = u
#                 q.append(self.graph[u][i])
#                 if (self.graph[u][i] == self.target):
#                     path = []
#                     crawl = self.target
#                     path.append(crawl)                        
#                     while (pred[crawl] != -1):
#                         # print(pred[crawl])
#                         path.append(pred[crawl])
#                         crawl = pred[crawl]
#                     return path

#     return []


# def FindPath(self,u):        
    #     for i in range(len(self.graph[u])):
    #         if self.visit[self.graph[u][i]] == -1:
    #             self.visit[self.graph[u][i]] = self.visit[u] + 1
    #             self.path[self.graph[u][i]] = u
    #             if u == self.target:
    #                 print("aaya")
    #                 return
    #             else:
    #                 self.route.append(self.graph[u][i])
    #     self.route.pop(0)
    #     if len(self.route) != 0:
    #         self.FindPath(self.route[0])
