def has_path(graph, start, end):
    if start not in graph:
        return False
    
    if start == end:
        return True
    
    def find_path(start, end, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        
        if start == end:
            return True
        
        if start in graph:
            for child in graph[start]:
                if child not in visited:
                    if find_path(child, end, visited):
                        return True
        return False
    
    return find_path(start, end)


graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': ['F'],
}

print(has_path(graph, 'A', 'E'))
print(has_path(graph, 'A', 'F'))
print(has_path(graph, 'B', 'F'))