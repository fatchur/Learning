from collections import deque

def bfs(graph, start): 
    visited = set()
    queue = deque([start]) 
    visited.add(start)

    while queue: 
        current = queue.popleft() 
        print (current, graph[current])

        for neighbor in graph[current]: 
            if neighbor not in visited: 
                queue.append(neighbor)
                visited.add(neighbor)

    print(visited)


if __name__ == "__main__": 
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E'],
    }

    bfs(graph, 'A')