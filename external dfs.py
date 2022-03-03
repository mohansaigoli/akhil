from collections import defaultdict
class graph:
    def __init__(self):
        self.graph=defaultdict(list)
def add_edge(self,u,v):
       self.graph[u].append(v)
def DFSUtil (self,v,visited):
         visited.add(v)
         print (v,end="  ")
for neighbour in self.graph[v]:
 if neighbour not in visited: 
    self.DFSUtil(neighbour,visited),
    def dfs (self,v):
       visited = set()
       self .DFSUtil (v,visited)
 g=graph()
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,2)
g.add_edge(2,0)
g.add_edge(2,3)
g.add_edge(3,3)
print("folowing is depth first search  travelling"" (starting from vertex")
g.dfs(2)          
           
           

       
