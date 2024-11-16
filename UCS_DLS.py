from collections import defaultdict, deque
import heapq

# Iterative Deepening Search (IDS)
def ids(graph, start, target):
    def dfs_limited(node, target, depth, visited, path):
        if depth < 0:
            return False
        visited.add(node)
        path.append(node)
        
        if node == target:
            return True
        
        for neighbor, _ in graph.get(node, []):
            if neighbor not in visited:
                if dfs_limited(neighbor, target, depth - 1, visited, path):
                    return True
        
        path.pop()  # Backtrack
        visited.remove(node)
        return False

    depth = 0
    while True:
        visited = set()
        path = []
        if dfs_limited(start, target, depth, visited, path):
            return True, path
        if len(visited) == len(graph):  # All nodes explored
            return False, []
        depth += 1

# Uniform Cost Search (UCS)
def ucs(graph, start, goal):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start, []))  # (cost, current_city, path)
    visited = set()

    while priority_queue:
        cost, current, path = heapq.heappop(priority_queue)

        if current in visited:
            continue
        visited.add(current)
        path = path + [current]

        if current == goal:
            return path, cost

        for neighbor, weight in graph.get(current, []):
            if neighbor not in visited:
                heapq.heappush(priority_queue, (cost + weight, neighbor, path))
    
    return [], float('inf')  # No path found

# Example Usage
graph = {
    "A": [("B", 1), ("C", 4)],
    "B": [("A", 1), ("D", 2), ("E", 5)],
    "C": [("A", 4), ("E", 1)],
    "D": [("B", 2)],
    "E": [("B", 5), ("C", 1)]
}

# Test IDS
start_city = "A"
target_city = "E"
found, path = ids(graph, start_city, target_city)
print(f"IDS: Found={found}, Path={path}")

# Test UCS
start_city = "A"
goal_city = "E"
path, cost = ucs(graph, start_city, goal_city)
print(f"UCS: Path={path}, Cost={cost}")
