def depth_limited_search(graph, start, goal, limit):
    stack = [(start, 0)]  # Stack to keep track of nodes with depth
    visited = list()  # List to keep track of visited nodes within the depth limit
    result = ["Goal not found within limit", list()]  # Default result

    # DFS loop with depth limit
    while stack:
        node, depth = stack.pop()  # Pop a node and its depth from the stack
        if node not in visited:
            visited.append(node)  # Mark node as visited

        # Check if goal node is found within the depth limit
        if node == goal:
            result[0] = "Goal found"  # Update the result
            break  # Exit loop if goal is found

        # If depth limit is not reached, add neighbors to the stack
        if depth < limit:
            for child in graph.get(node, []):
                if child not in visited:
                    stack.append((child, depth + 1))

    # Final result, including visited nodes within the depth limit
    result[1] = visited
    return result

# Updated graph based on the provided tree structure
graph_updated = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'E': ['F', 'G']
}

# Perform Depth Limited Search with various limits
for limit in range(1, 5):  # Testing limits from 1 to 4
    result = depth_limited_search(graph_updated, 'A', 'F', limit)
    print(f"Depth Limit {limit}:")
    print(f"  Goal Status: {result[0]}")
    print(f"  Visited Nodes: {result[1]}\n")
