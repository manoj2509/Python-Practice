__author__ = 'Mj'


def findAllPath(graph, start, end, path=[]):
    path = path + [start]

    if start == end:
        return path
    if not start in graph:
        return None
    paths = []
    for node in graph[start]:
        if node not in path:                                #not getting in a loop
            newpath = findAllPath(graph, node, end, path)
            paths.append(newpath)
    return paths


def shortestPath(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not start in graph:
        return None
    shortest = []
    for node in graph[start]:
        if node not in path:
            newpath = shortestPath(graph, node, end, path)
            if not shortest or len(shortest) > len(newpath):
                shortest = newpath
    return shortest
graph = {}
'''n1, n2 = input().split()
    graph.setdefault(n1, []).append((n2, d))        //for weighted graph
    graph.setdefault(n2, []).append((n1, d))        //back-connection because undirected'''
numEdges = int(input())
for i in range(numEdges):
    n1, n2 = list(map(int, input().strip().split()))
    '''For integer listed input'''
    graph.setdefault(n1, []).append(n2)
    #graph.setdefault(n2, []).append(n1)
s, e = list(map(int, input("Enter start and end: ").strip().split()))
val = findAllPath(graph, s, e)
print(val)
val = shortestPath(graph, s, e)
print(val)
'''for v in range(1, limit):
    print(v,': ', graph[v])
print(graph)'''