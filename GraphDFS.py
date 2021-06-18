#This Program helps you to traverse the Graph in deapthward motion (to visit each node) using DFS
from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addEdge(self, u, v):
        self.graph[u].append(v)
    def DFSUtil(self, v, visited):
        visited.add(v)
        print(v, end=" ")
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)
    def DFS(self, v):
        visited=set()
        self.DFSUtil(v, visited)

g=Graph()
edge=int(input("Enter the number of Edges= "))
for x in range(edge):
    u=int(input("Enter node a:"))
    v=int(input("Enter node b:"))
    g.addEdge(u, v)
n = int(input("Enter the starting node: "))
print("Following is DFS from (starting from vertex ",n,")")
g.DFS(n)
