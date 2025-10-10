from collections import deque  


def dfs(graph, start, visited): 
    stack = deque([start]) 
    visited.add(start)

    while stack: 
        current = stack.pop() 

        for neighbor in graph[current]: 
            if neighbor not in visited: 
                stack.append(neighbor)
                visited.add(neighbor)

                dfs(graph, neighbor, visited)


if __name__ == "__main__": 
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E'],
    }

    visited = set()
    dfs(graph, 'A', visited)
    print(visited)