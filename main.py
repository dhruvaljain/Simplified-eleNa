import sys
from algorithms import BFS 
from algorithms import DFS 


src = int(sys.argv[1])
target = int(sys.argv[2])
algo = sys.argv[3]
N_DFS = 10
N_BFS = 10000
if algo == "BFS":
    if src > N_BFS or target > N_BFS:
        print("source or target must be less than",N_BFS)
    else:    
        x = BFS(src,target,algo)
        print("Constructed Directed Graph :")
        print(x.graph[1:])
        path = x.FindPath(src)
        if len(path) == 1:
            print("No path between source and target exist")
        else:
            print("The shortest path is :")
            print(path)
else:
    if src > N_DFS or target > N_DFS:
        print("source or target must be less than",N_DFS)
    else:
        x = DFS(src,target,algo)
        print("Constructed Directed Graph :")
        print(x.graph[1:])
        x.FindPath(src)        
        if len(x.path) == 1:
            print("No path between source and target exist")
        else:
            print("The shortest path is :")
            print(x.path)
