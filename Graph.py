from collections import defaultdict
graph=defaultdict(list)       #Defaultdict is a sub-class of the dict class that returns a dictionary-like object. 
def addEdge(graph, u, v):
    graph[u].append(v)
def generate_edge(graph):
    edges=[]
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))
    return edges

n = int(input("Enter the number of edges you want to create: "))
for x in range(n):
    u = input("Enter the value of node a:")
    v = input("Enter the value of node b:")
    addEdge(graph, u, v)    
print(generate_edge(graph))


