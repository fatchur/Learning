from collections import deque


visited = []
path = []
current_distance = 0

def dfs_weight(graph, start, max_distance): 

    if start in visited:
        return

    visited.append(start)
    path.append(start)

    global current_distance
    if current_distance > max_distance: 
        return 

    if current_distance == max_distance: 
        print (">>>>", path, current_distance)
        return 
    
    print ("...", visited, current_distance)
    print (start, graph[start])

    for neighbor, wight in graph[start]: 
        if neighbor not in visited: 
            current_distance += wight
            dfs_weight(graph, neighbor, max_distance)
            current_distance -= wight
            path.pop()


if __name__ == "__main__": 
    graph = {
        'A': [('B', 1), ('C', 2)],
        'B': [('A', 1), ('D', 3), ('E', 4)],
        'C': [('A', 2), ('F', 5)],
        'D': [('B', 3)],
        'E': [('B', 4), ('F', 5)],
        'F': [('C', 5), ('E', 5)],
    }

    
    start = 'A'
    max_distance = 5
    dfs_weight(graph, start, max_distance)
    print (visited)
