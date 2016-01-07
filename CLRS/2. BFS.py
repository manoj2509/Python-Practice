__author__ = 'Mj'


def BFS(graph, source):
    k = 0
    visited.append(source)
    level.setdefault(str(k), []).append(source)
    enqueue = [source]
    while enqueue:
        k += 1
        for node in graph.get(enqueue[0], []):
            if node not in graph and node not in visited:
                enqueue.append(node)
                level.setdefault(str(k), []).append(node)
                parent['Node ' + str(node)] = enqueue[0]
                visited.append(node)
                break
            if node not in visited:
                enqueue.append(node)
                level.setdefault(str(k), []).append(node)
                parent['Node ' + str(node)] = enqueue[0]
                visited.append(node)
        enqueue.pop(0)


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
BFS(Graph, so)
print(level)
print(parent)
print(visited)