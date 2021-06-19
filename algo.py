from numpy import inf as infinity

my_val = {
    'B': {'A': 5, 'D': 1, 'G': 2},
    'A': {'B': 5, 'D': 3, 'E': 12, 'F': 5},
    'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
    'G': {'B': 2, 'D': 1, 'C': 2},
    'C': {'G': 2, 'E': 1, 'F': 16},
    'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2},
    'F': {'A': 5, 'E': 2, 'C': 16}}


def dijkstra_algo(graph, start_node, goal_node):
    shortest = {}
    track_pre = {}
    unvisited_node = graph
    path = []

    for node in unvisited_node:
        shortest[node] = infinity
    shortest[start_node] = 0

    while unvisited_node:
        minDistance = None

        for node in unvisited_node:
            if minDistance is None:
                minDistance = node
            elif shortest[node] < shortest[minDistance]:
                minDistance = node

        pathway = graph[minDistance].items()

        for child_node_distance, weight in pathway:
            if weight + shortest[minDistance] < shortest[child_node_distance]:
                shortest[child_node_distance] = weight + shortest[minDistance]
                track_pre[child_node_distance] = minDistance

        unvisited_node.pop(minDistance)

    current_node = goal_node

    while current_node != start_node:
        try:
            path.insert(0, current_node)
            current_node = track_pre[current_node]
        except KeyError:
            print("Can't reach")
            break

    path.insert(0, start_node)

    if shortest[goal_node] != infinity:
        print("Cost: " + str(shortest[goal_node]) + "\nPath: " + str(path))


dijkstra_algo(my_val, 'B', 'C')
