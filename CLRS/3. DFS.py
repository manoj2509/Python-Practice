__author__ = 'Mj'


def DFS(graph, source, k):
    visited.append(source)
    level.setdefault(str(k), []).append(source)
    if source not in graph:
        return None
    for node in graph[source]:
        if node in visited:
            print("Cycle present between", node, source)
        if node not in visited:
            parent['Node ' + str(node)] = source
            DFS(graph, node, k+1)

Graph = {}
visited = []
level = {}
parent = {}
numEdges = int(input().strip())
for i in range(numEdges):
    n1, n2 = list(map(int, input().strip().split()))
    Graph.setdefault(n1, []).append(n2)
so = int(input("Enter source: "))
parent['Node ' + str(so)] = None
DFS(Graph, so, 0)
print(level)
print(parent)
print(visited)