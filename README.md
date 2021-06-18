# Introduction to Graphs
Graph is a non-linear Data Structure which consist of set of objects called nodes/vertices connected by set of edges.

![image](https://user-images.githubusercontent.com/72907502/122525958-674fe500-d037-11eb-94ff-0fbd41aa9b9e.png)

## Types Of Graphs:
1. Weighted Graph: If a weight is associated with each edge in a graph is called a weighted graph. Edges value can represent weight/cost/length.
2. Unweighted Graph: Where there is no value or weight associated with the edge. By default, all the graphs are unweighted unless there is a value associated. 
3. Directed Graph/Digraph: A Graph where all the edges are directed from one node to another.
4. Undirected Graph: Where a set of objects are connected, and all the edges are bidirectional.

## Applications of Graphs:
1. World Wide Web can be represented as a digraph if page A had link to page B.
2. Traffic Patterns can be modeled (The entire premise of Google Maps is using a big giant graph with nodes and edges to figure out fastest or shortest way to travel.)
3. In computer science graphs are used to show flow of computation.

## Graph Traversal
It refers to the process of visiting each node/vertex in graph.
### Methods for Graph Traversal
1. Breadth First search (BFS): Breadth First Search (BFS) algorithm traverses a graph in a breadthward motion and uses a queue to remember to get the next vertex to start a search, when a dead end occurs in any iteration.

2. Depth First Search (DFS): It travels the graph in depthward motion and uses a stack to remember to get the next vertex to start a search, when a dead end occurs in any iteration.

## All Pair Shortest Path / Floyd Warshall Algorithm
Used to find a all pair shortest path problem from a given weighted graph. 
#### Function Used: 
```
def floyd_warshall(G):
    distance=list(map(lambda i:list(map(lambda j:j,i)), G))
    for k in range(n):
        for i in range(n):
            for j in range(n):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
```


