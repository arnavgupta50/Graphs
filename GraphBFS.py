from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addEdge(self, u, v):
        self.graph[u].append(v)
    def BFS(self, s):
        visited=[False]*(max(self.graph)+1)
        queue=[]
        queue.append(s)
        visited[s]=True
        while queue:
            s=queue.pop(0)
            print(s, end=" ")
            for i in self.graph[s]:
                if visited[i]==False:
                    queue.append(i)
                    visited[i]=True

g = Graph()
edge=int(input("Enter the number of Edges= "))
for x in range(edge):                           #Enter the nodes which you want to link eg. 1------2
    u=int(input("Enter node a:"))
    v=int(input("Enter node b:"))
    g.addEdge(u, v)
n = int(input("Enter the starting node: "))
print ("Following is Breadth First Traversal"
                  " (starting from vertex ", n, "): ")
g.BFS(n)
