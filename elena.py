import random


class Graph():
# Class Graph is responsible for generating the random directed graph by taking the type of routing algorithm into account.
# Due to time complexity constraint, the maximum allowable vertices is kept 10 in case of DFS algorithm. While, for BFS it is
# 10000.
    def __init__(self, algo):
        if algo == "BFS":
            self.N = 10000
        else:
            self.N = 10
        self.EDGE_LIMIT = 10
        self.algo = algo
        self.graph = self.generate_graph()

    # The generate_graph function builds the graph. EDGE_LIMIT is set to 10, which means that a vertex can have atmost 10 edges
    # to other vertices.
    def generate_graph(self):
        graph = [[]]
        num_edges = [random.randrange(0, self.EDGE_LIMIT, 1) for i in range(self.N)]        
        for edge in num_edges:
            graph.append([random.randrange(1, self.N+1, 1) for i in range(edge)])
        return graph
        
    
class search():
    # search class is an abstract class which is implemented by class BFS and DFS indiviually. 
    # The FindPath function implements the actual routing algorithm.
    # The constructor initialises the variables required by the routing classes BFS and DFS.

    def __init__(self,source, target, algo):
        self.graph = Graph(algo).graph        
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




    

