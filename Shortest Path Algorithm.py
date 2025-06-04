Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> my_graph = {
...     'A': [('B', 5), ('C', 3), ('E', 11)],
...     'B': [('A', 5), ('C', 1), ('F', 2)],
...     'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
...     'D': [('C',1 ), ('E', 9), ('F', 3)],
...     'E': [('A', 11), ('C', 5), ('D', 9)],
...     'F': [('B', 2), ('D', 3)]
... }
... 
... def shortest_path(graph, start, target = ''):
...     unvisited = list(graph)
...     distances = {node: 0 if node == start else float('inf') for node in graph}
...     paths = {node: [] for node in graph}
...     paths[start].append(start)
...     
...     while unvisited:
...         current = min(unvisited, key=distances.get)
...         for node, distance in graph[current]:
...             if distance + distances[current] < distances[node]:
...                 distances[node] = distance + distances[current]
...                 if paths[node] and paths[node][-1] == node:
...                     paths[node] = paths[current][:]
...                 else:
...                     paths[node].extend(paths[current])
...                 paths[node].append(node)
...         unvisited.remove(current)
...     
...     targets_to_print = [target] if target else graph
...     for node in targets_to_print:
...         if node == start:
...             continue
...         print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')
...     
...     return distances, paths
...     
