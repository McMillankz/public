import random
n = 6
p = 0.2
G = [[0, 0, 1, 1, 1, 0],
     [0, 0, 0, 1, 0, 1],
     [1, 0, 0, 1, 1, 0],
     [1, 1, 1, 1, 0, 0],
     [1, 0, 1, 0, 0, 1],
     [0, 1, 0, 0, 1, 0]] 
V = list(range(n))

# for i in range(n):
#     for j in range(i+1, n):
#         if random.random() < p:
#             G[i][j] = 1
#             G[j][i] = 1

def DFS(graph, begin, end, visited = None, start = None):
    if visited is None:
        visited = []
    if start is None:
        start = [begin]

    visited.append(begin)

    if begin == end:
        print ("Связь найдена, путь: ", end = "")
        for elem in start:
            print (elem, end=" ")
        print()
        return

    for elem in range(len(graph[V.index(begin)])):
        if graph[V.index(begin)][V.index(V[elem])] == 1 and V[elem] not in visited:
            DFS (graph, V[elem], end, visited, start + [V[elem]])
    

begin = 0
end = 5

DFS(G, begin, end)