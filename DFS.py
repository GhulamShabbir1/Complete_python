def dfs(graph, start, dest):
    stack = list()  # Stack to keep track of the nodes
    visited = list()  # List to track visited nodes
    stack.append(start)  # Start DFS from the start node
    visited.append(start)  # Mark the start node as visited
    print("Visited", start)
    
    result = ["Destination not found", list()]  # Default result

    # DFS loop
    while stack:
        node = stack.pop()  # Pop a node from the stack
        
        if node == dest:
            print(f"Destination node found: {node}")
            result[0] = "Destination found"  # Update the result
            break  # Exit the loop if destination is found
        
        print(f"{node} is not the destination node.")
        
        # Traverse all unvisited neighbors
        for child in graph[node]:
            if child not in visited:
                visited.append(child)
                stack.append(child)
    
    # Final result, including visited nodes
    result[1] = visited
    return result

# Graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': [ 'F'],
    'D': ['G'],
    'E': ['H','I'],
    'F': ['J']
}

# Example usage: Start DFS from node 'A' and search for node 'E'
start_node = 'A'
destination_node = 'F'

result = dfs(graph, start_node, destination_node)

# Output the result
print("\nDFS Result:")
print(f"Destination Status: {result[0]}")
print(f"Visited Nodes: {result[1]}")