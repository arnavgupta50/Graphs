#This program is used to find the shortest path between two nodes in a weighted graph using Floyd Warshall Algorithm
n = int(input("Enter the number of edges= "))
INF=999999
def floyd_warshall(G):
    distance=list(map(lambda i:list(map(lambda j:j,i)), G))
    for k in range(n):
        for i in range(n):
            for j in range(n):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    print_solution(distance)

def print_solution(distance):
    for i in range(n):
        for j in range(n):
            if(distance[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distance[i][j], end=" ")
        print(" ")    
G = [[0, 3, INF, 5],
         [2, 0, INF, 4],
         [INF, 1, 0, INF],
         [INF, INF, 2, 0]]
floyd_warshall(G)
